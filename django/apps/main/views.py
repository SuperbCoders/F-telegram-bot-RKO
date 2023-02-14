from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from djangorestframework_camel_case.parser import (
    CamelCaseFormParser,
    CamelCaseMultiPartParser,
    CamelCaseJSONParser,
)
import requests

from .utils import format_phone, generate_code

from .adapter import Adapter_LoanRequest

import uuid
from datetime import date

from .models import (
    LoanRequest,
    User,
    DocumentFile,
)
from .serializers import (
    # LoanApplicationSerializer,
    LoanRequestSerializer,
)
import os


class LoanRequestCurrentAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser,
                      CamelCaseJSONParser]
    renderer_classes = [CamelCaseJSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        phone_number: str | None = kwargs.get("phone_number")
        if phone_number:
            phone_number = format_phone(phone_number)

        loan_request = LoanRequest.objects.filter(
            contact_number=phone_number,
            is_finished=False,
        ).first()

        if loan_request:
            loan_request_serializer = LoanRequestSerializer(loan_request)
            return JsonResponse(loan_request_serializer.data)
        else:
            return Response({}, status=status.HTTP_200_OK)

    def post(self, request, format=None, *args, **kwargs):
        phone_number = kwargs.get("phone_number")
        phone_number = format_phone(phone_number)
        data = request.data

        print(data)

        if 'contact_number' in data:
            data['contact_number'] = format_phone(data['contact_number'])

        loan_request = LoanRequest.objects.filter(
            contact_number=phone_number,
            is_finished=False,
        ).first()

        if loan_request:
            for field_name, field_value in data.items():
                setattr(loan_request, field_name, field_value)
                loan_request.save()
        else:
            loan_request = LoanRequest(**data)
            loan_request.save()
        if os.getenv("DJANGO_APP_API_BANK_ENABLE") == 'enable':
            if loan_request.is_finished:
                adapter = Adapter_LoanRequest(loan_request)
                result = adapter.getResult()
                print("DJANGO_APP_API_BANK result", result)
                answer = requests.post(
                    os.getenv("DJANGO_APP_API_BANK") + '/order/rko', json=result)
                print("DJANGO_APP_API_BANK answer",
                      answer.status_code, answer.text)

                orderId = answer['orderId']
                loan_request.order_id = orderId
                response_status = requests.get(
                    os.getenv("DJANGO_APP_API_BANK") + f'/order/{orderId}')
                data_status = response_status.json()
                loan_request.status = data_status['statusCode']
                loan_request.last_status = data_status['statusCode']
                loan_request.status_description = data_status['statusDescription']

                loan_request.save()
        return Response({}, status=status.HTTP_200_OK)


class LoanApplicationListAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser,
                      CamelCaseJSONParser]
    renderer_classes = [CamelCaseJSONRenderer]
    model = LoanRequest
    serializer_class = LoanRequestSerializer

    def get_queryset(self):
        telegram_chat_id = self.request.GET.get('telegram_chat_id')
        phone_number = self.request.GET.get('phone_number')
        if telegram_chat_id:
            user = User.objects.filter(
                telegram_chat_id=telegram_chat_id).first()
            phone_number = user.phone_number

        return (
            LoanRequest.objects.filter(
                contact_number=format_phone(phone_number),
                is_finished=True,
            ).order_by("created_at")
        )


class LoanApplicationStatusListAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser,
                      CamelCaseJSONParser]
    renderer_classes = [CamelCaseJSONRenderer]
    model = LoanRequest
    serializer_class = LoanRequestSerializer

    def get_queryset(self):
        telegram_chat_id = self.request.GET.get('telegram_chat_id')
        phone_number = self.request.GET.get('phone_number')
        if telegram_chat_id:
            user = User.objects.filter(
                telegram_chat_id=telegram_chat_id).first()
            phone_number = user.phone_number

        loan_request = LoanRequest.objects.filter(
            contact_number=format_phone(phone_number),
            is_finished=True,
            order_id__isnull=False,
        ).order_by("created_at")

        list_status = []

        if os.getenv("DJANGO_APP_API_BANK_ENABLE") in ['enable', 'test']:
            for load in loan_request:

                response = requests.get(
                    os.getenv("DJANGO_APP_API_BANK") + f"/order/{load.order_id}")
                print(response.text)
                responseData = response.json()
                list_status.append({
                    "accountCurrency": responseData["accountCurrency"],
                    "accountNumber": responseData["accountNumber"],
                    "accountReservationDate": responseData["accountReservationDate"],
                    "accountStatus": responseData["accountStatus"],
                    "orderCreatedDate": responseData["orderCreatedDate"],
                    "orderNumber": responseData["orderNumber"],
                    "orderStatus": responseData["orderStatus"],
                    "orderType": responseData["orderType"],
                    "companyName": responseData["orderType"],
                    "inn": responseData["orderType"],
                    "ogrn": responseData["orderType"],

                })

        return list_status


class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        telegram_chat_id = kwargs.get("telegram_chat_id")

        list_user = User.objects.filter(telegram_chat_id=telegram_chat_id)
        if len(list_user) == 1:
            return Response({}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None, *args, **kwargs):
        telegram_chat_id = self.kwargs.get("telegram_chat_id")
        phone_number = self.request.data.get("phone_number")
        try:
            user = User(
                username=uuid.uuid4(),
                password=uuid.uuid4(),
                phone_number=phone_number,
                telegram_chat_id=telegram_chat_id
            )
            user.save()
            return Response({}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, format=None, *args, **kwargs):
    #     telegram_chat_id = self.kwargs.get("telegram_chat_id")
    #     try:
    #         User.objects.get(telegram_chat_id=telegram_chat_id)
    #         return Response({}, status=status.HTTP_200_OK)
    #     except User.DoesNotExist:
    #         return Response({}, status=status.HTTP_400_BAD_REQUEST)


class PhoneApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        telegram_chat_id = kwargs.get("telegram_chat_id")
        list_user = User.objects.filter(telegram_chat_id=telegram_chat_id)
        if len(list_user) == 1:
            return Response({
                'phone': list_user[0].phone_number
            }, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class DocumentLoad(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None, *args, **kwargs):
        documents = request.FILES
        paths = []
        for file_name in documents:
            file = request.FILES.get(file_name)
            document_model = DocumentFile(document=file)
            document_model.save()
            paths.append({
                "path": document_model.document.url
            })
        return Response({
            "images": paths,
        }, status=status.HTTP_200_OK)


class StatusCheck(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        loan_request = LoanRequest.objects.filter(is_finished=True)
        for lr in loan_request:
            order_id = lr.order_id
            if os.getenv("DJANGO_APP_API_BANK_ENABLE") in ['enable', 'test']:
                if os.getenv("DJANGO_APP_API_BANK_ENABLE") == 'test':
                    responseData = {
                        "statusCode": 'under_review',
                        "statusDescription": 'На рассмотрении',
                    }
                else:
                    response = requests.get(
                        os.getenv("DJANGO_APP_API_BANK") + f"/order/{order_id}")
                    responseData = response.json()

                lr.status = responseData["orderStatus"]['statusCode']
                lr.status_description = responseData["orderStatus"]['statusDescription']
                lr.save()

        return Response({}, status=status.HTTP_200_OK)


class SmsValidation(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None, *args, **kwargs):
        phone_number = kwargs['phone_number']
        user = User.objects.filter(
            phone_number=format_phone(phone_number)
        ).first()

        code_is_frontend = request.data['code']
        code_is_user = user.last_sms_code

        if code_is_frontend == code_is_user:
            return Response({}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, format=None, *args, **kwargs):
        phone_number = kwargs['phone_number']
        user = User.objects.filter(
            phone_number=format_phone(phone_number)
        ).first()
        code = generate_code()
        user.last_sms_code = code
        user.save()
        sms_url = os.getenv("SMS_URL")
        message = os.getenv("SMS_MESSAGE").format(code=f"{code}")
        if os.getenv("DJANGO_APP_API_BANK_ENABLE") == 'enable':
            requests.get(sms_url, json={
                "processId": f"+{phone_number}",
                "taskId": "0",
                "phone": f"+{phone_number}",
                "priority": "LOW",
                "message": message
            })
        return Response({}, status=status.HTTP_200_OK)
