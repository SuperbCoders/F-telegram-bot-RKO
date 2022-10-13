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
    LoanApplication,
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


# class LoanApplicationListAPIView(ListAPIView):
#     permission_classes = [permissions.AllowAny]
#     parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser,
#                       CamelCaseJSONParser]
#     renderer_classes = [CamelCaseJSONRenderer]
#     model = LoanApplication
#     serializer_class = LoanApplicationSerializer

    def get_queryset(self):
        telegram_chat_id = self.kwargs['telegram_chat_id']
        return (
            LoanApplication.objects
            .filter(telegram_chat_id=telegram_chat_id)
            .order_by("created_at")
        )

class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        telegram_chat_id = kwargs.get("telegram_chat_id")
        user = get_object_or_404(User, telegram_chat_id=telegram_chat_id)
        return Response({}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None, *args, **kwargs):
        telegram_chat_id = self.kwargs.get("telegram_chat_id")
        phone_number = self.request.data.get("phone_number")
        print(telegram_chat_id, phone_number)
        print(User.objects.all())
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
