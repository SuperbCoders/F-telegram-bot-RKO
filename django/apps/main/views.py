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

from .utils import format_phone

from .adapter import Adapter_LoanRequest

import uuid
from datetime import date

from .models import (
    LoanRequest,
    User,
    PassportFile,
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
                answer = requests.post(os.getenv("DJANGO_APP_API_BANK") + '/order/rko', json=result)
                print("DJANGO_APP_API_BANK answer", answer.status_code, answer.text)
                
                orderId = answer['orderId']
                loan_request.order_id = orderId
                response_status = requests.get(os.getenv("DJANGO_APP_API_BANK") + f'/order/{orderId}')
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
        telegram_chat_id = self.kwargs['telegram_chat_id']
        user = User.objects.filter(telegram_chat_id=telegram_chat_id).first()
        
        return (
            LoanRequest.objects.filter(
                contact_number=format_phone(user.phone_number),
                is_finished=True,
            ).order_by("created_at")
        )

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


class PassportLoad(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None, *args, **kwargs):
        passport = request.FILES.get("passport")
        passport_model = PassportFile(passport=passport)
        passport_model.save()

        return Response({
            "path": passport_model.passport.url
        }, status=status.HTTP_200_OK)

class StatusCheck(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None, *args, **kwargs):
        loan_request = LoanRequest.objects.filter(is_finished=True)
        for lr in loan_request:
            order_id = lr.order_id
            if os.getenv("DJANGO_APP_API_BANK_ENABLE") == 'enable':
                response = requests.get( os.getenv("DJANGO_APP_API_BANK") + f"/order/{order_id}" )
                responseData = response.json()
                lr.status = responseData['statusCode']
                lr.status_description = responseData['statusDescription']
                lr.save()
        return Response({}, status=status.HTTP_200_OK)