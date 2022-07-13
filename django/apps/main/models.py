from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .tasks import send_telegram_bot_message


class User(AbstractUser):
    pass


class LoanApplication(models.Model):
    STATUS_CHOICES = [
        ("under_review", "На рассмотрении"),
        ("declined", "Отклонена"),
        ("approved", "Одобрена"),
    ]
    status = models.CharField(max_length=140, choices=STATUS_CHOICES,
                              default="under_review", blank=True)
    loan_amount = models.IntegerField(blank=True, null=True)
    loan_term = models.IntegerField(blank=True, null=True)
    loan_region = models.CharField(max_length=140, blank=True)
    name = models.CharField(max_length=140, blank=True)
    city = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    old_name = models.CharField(max_length=140, blank=True)
    passport_photo_one = models.ImageField(
        upload_to="passport",
        blank=True,
        null=True,
    )
    passport_photo_two = models.ImageField(
        upload_to="passport",
        blank=True,
        null=True,
    )
    passport_photo_three = models.ImageField(
        upload_to="passport",
        blank=True,
        null=True,
    )
    passport_photo_four = models.ImageField(
        upload_to="passport",
        blank=True,
        null=True,
    )
    passport_photo_five = models.ImageField(
        upload_to="passport",
        blank=True,
        null=True,
    )
    passport_series = models.CharField(max_length=140, blank=True)
    passport_number = models.CharField(max_length=140, blank=True)
    passport_issue_date = models.DateField(blank=True, null=True)
    passport_code = models.CharField(max_length=140, blank=True)
    passport_issued_by = models.CharField(max_length=140, blank=True)
    passport_place_of_birth = models.CharField(
        max_length=140,
        blank=True,
    )
    passport_date_of_birth = models.DateField(blank=True, null=True)
    old_passport_series = models.CharField(max_length=140, blank=True)
    old_passport_number = models.CharField(max_length=140, blank=True)
    old_passport_issue_date = models.DateField(blank=True, null=True)
    old_passport_code = models.CharField(max_length=140, blank=True)
    old_passport_issued_by = models.CharField(max_length=140, blank=True)
    old_passport_place_of_birth = models.CharField(
        max_length=140,
        blank=True,
    )
    old_passport_date_of_birth = models.DateField(blank=True, null=True)
    current_address = models.CharField(max_length=280, blank=True)
    current_apartments_number = models.CharField(max_length=140, blank=True)
    has_no_current_address = models.BooleanField(default=False)
    registration_address = models.CharField(max_length=280, blank=True)
    registration_apartments_number = models.CharField(
        max_length=140,
        blank=True,
    )
    monthly_income = models.IntegerField(blank=True, null=True)
    telegram_chat_id = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def _send_success_message_to_telegram(self):
        text = (
            "Ваша заявка отправлена в банк на рассмотрение.\n" +
            "Информация с результатами рассмотрения будет отправлена " +
            "вам по телефону и электронной почте."
        )
        send_telegram_bot_message.delay(self.telegram_chat_id, text)

    def _send_upload_message_to_telegram(self):
        text = (
            "Для успешного рассмотрения заявки банку необходимы " +
            "дополнительные документы. Пожалуйста, перейдите по " +
            "ссылке на сайт банка и загрузите их."
        )
        button_text = "Загрузить документы"
        button_url = "https://www.zenit.ru/"
        send_telegram_bot_message.delay(
            self.telegram_chat_id,
            text,
            button_url=button_url,
            button_text=button_text,
            delay=60,
        )

    class Meta:
        verbose_name = 'заявление'
        verbose_name_plural = "заявления"

    def save(self, *args, **kwargs):
        if not self.pk:
            self._send_success_message_to_telegram()
            self._send_upload_message_to_telegram()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
