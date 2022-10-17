from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from djangorestframework_camel_case.parser import (
    CamelCaseFormParser,
    CamelCaseMultiPartParser,
    CamelCaseJSONParser,
)

import uuid

from .models import (
    LoanRequest,
    User,
)
from .serializers import (
    # LoanApplicationSerializer,
    LoanRequestSerializer,
)


class LoanRequestCreateAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser,
                      CamelCaseJSONParser]
    renderer_classes = [CamelCaseJSONRenderer]
    model = LoanRequest
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer


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
        print(user.phone_number)
        pn = user.phone_number
        phone_number_format = f"+{pn[1]} ({pn[2]}{pn[3]}{pn[4]}) {pn[5]}{pn[6]}{pn[7]} {pn[8]}{pn[9]} {pn[10]}{pn[11]}"
        return (
            LoanRequest.objects
            .filter(contact_number=phone_number_format)
            .order_by("created_at")
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