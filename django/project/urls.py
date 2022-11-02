"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.main.views import (
    # LoanApplicationCreateAPIView,
    UserAPIView,
    PhoneApiView,
    LicensionApiView,
    LoanRequestCurrentAPIView,
    LoanApplicationListAPIView,
)


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(
        "api/loan-application/current/<str:phone_number>/",
        LoanRequestCurrentAPIView.as_view()
    ),
    path(
        "api/loan-application/<int:telegram_chat_id>/",
        LoanApplicationListAPIView.as_view()
    ),
    path(
        "api/user/<str:telegram_chat_id>/",
        UserAPIView.as_view(),
    ),
    path('adminpage/', admin.site.urls),
    path('api/get_phone/<str:telegram_chat_id>/', PhoneApiView.as_view()),
    path('api/get_license/', LicensionApiView.as_view()),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
