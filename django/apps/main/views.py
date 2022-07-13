from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView

from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from djangorestframework_camel_case.parser import (
    CamelCaseFormParser,
    CamelCaseMultiPartParser,
    CamelCaseJSONParser,
)

from .models import (
    LoanApplication,
)
from .serializers import (
    LoanApplicationSerializer,
)


class LoanApplicationCreateAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser,
                      CamelCaseJSONParser]
    renderer_classes = [CamelCaseJSONRenderer]
    model = LoanApplication
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer


class LoanApplicationListAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser,
                      CamelCaseJSONParser]
    renderer_classes = [CamelCaseJSONRenderer]
    model = LoanApplication
    serializer_class = LoanApplicationSerializer

    def get_queryset(self):
        telegram_chat_id = self.kwargs['telegram_chat_id']
        return (
            LoanApplication.objects
            .filter(telegram_chat_id=telegram_chat_id)
            .order_by("created_at")
        )
