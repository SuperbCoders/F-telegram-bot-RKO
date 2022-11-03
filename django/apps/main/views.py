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

import uuid
from datetime import date

from .models import (
    LoanRequest,
    User,
)
from .serializers import (
    # LoanApplicationSerializer,
    LoanRequestSerializer,
)


class LoanRequestCurrentAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser,
                      CamelCaseJSONParser]
    renderer_classes = [CamelCaseJSONRenderer]
    
    def get(self, request, format=None, *args, **kwargs):
        phone_number: str | None = kwargs.get("phone_number")
        if phone_number:
            pn = phone_number.strip()
            phone_number = f"+{pn[0]} ({pn[1]}{pn[2]}{pn[3]}) {pn[4]}{pn[5]}{pn[6]} {pn[7]}{pn[8]} {pn[9]}{pn[10]}"
        
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
        data = request.data
        
        print(data)
        
        loan_request = LoanRequest.objects.filter(
            contact_number=phone_number,
            is_finished=False,
        ).first()
        
        if loan_request:
            for field_name, field_value in data.items():
                setattr(loan_request, field_name, field_value)
                loan_request.save()
        else:
            new_load_request = LoanRequest(**data)
            new_load_request.save()
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
        pn = user.phone_number
        phone_number_format = f"+{pn[1]} ({pn[2]}{pn[3]}{pn[4]}) {pn[5]}{pn[6]}{pn[7]} {pn[8]}{pn[9]} {pn[10]}{pn[11]}"
        return (
            LoanRequest.objects.filter(
                contact_number=phone_number_format,
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


class LicensionApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        return Response({
            "view": "Вид",
            "number": 25432634,
            "Issued_by": "Выдан Московским департаментом",
            "License_issue_date": date.today(),
            "Validity": date.today(),
            "List_types_licensed_activities": "Перечни",
        }, status=status.HTTP_200_OK)