from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from rest_framework.authtoken.models import Token

from .models import User, LoanApplication
from .tasks import send_telegram_bot_message


class UserAdmin(BaseUserAdmin):
    pass


class LoanApplicationAdmin(admin.ModelAdmin):
    model = LoanApplication
    list_display = ["email", "status"]
    readonly_fields = ["status"]
    actions = [
        'status_approved',
        'status_declined',
    ]

    def status_approved(self, request, queryset):
        for application in queryset:
            application.status = "approved"
            application.save()
            send_telegram_bot_message.delay(
                application.telegram_chat_id,
                "Ваша заявка была одобрена банком."
            )
    status_approved.short_description = (
        "Одобрить выбранные заявления"
    )

    def status_declined(self, request, queryset):
        for application in queryset:
            application.status = "declined"
            application.save()
            send_telegram_bot_message.delay(
                application.telegram_chat_id,
                "К сожалению ваша заявка была отклонена банком."
            )
    status_declined.short_description = (
        "Отклонить выбранные заявления"
    )


admin.site.register(LoanApplication, LoanApplicationAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)
