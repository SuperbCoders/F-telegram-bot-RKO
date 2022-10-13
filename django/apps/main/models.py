import random
import string

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .tasks import send_telegram_bot_message

INN_MAX_LENGTH = 12
MAX_CITY_NAME_STRING = 30
MAX_STRING_LENGTH = 100
MAX_PHONE_LENGTH = 12
MAX_ADDRESS_LENGTH = 120
MAX_JSON_STRING_LENGTH = 300

def generate_dhl_track_id():
    characters = string.ascii_uppercase + string.digits
    random_dhl_track_id = ''.join(
        random.choice(characters) for _ in range(15)
    )
    return random_dhl_track_id

def generate_application_id():
    characters = ''.join(
        random.choice(string.ascii_uppercase) for _ in range(2)
    )
    digits = ''.join(
        random.choice(string.digits) for _ in range(6)
    )
    return f"{characters}-{digits}"


class TypeToChoose(models.Model):
    type_name = models.CharField(max_length=MAX_CITY_NAME_STRING)

class TariffPlan(models.Model):
    name = models.CharField(max_length=MAX_CITY_NAME_STRING)
    limit_descr = models.CharField(max_length=MAX_STRING_LENGTH)
    transaction_policy = models.CharField(max_length=MAX_STRING_LENGTH)
    payment_policy = models.CharField(max_length=MAX_STRING_LENGTH)
    price = models.IntegerField()


class LoanRequest(models.Model):
    STATUS_CHOICES = [
        ("under_review", "На рассмотрении"),
        ("declined", "Отклонена"),
        ("approved", "Одобрена"),
    ]
    status = models.CharField(max_length=140,
                              choices=STATUS_CHOICES,
                              default="under_review",
                              blank=True)
    inn = models.CharField(max_length=INN_MAX_LENGTH)
    company_name = models.CharField(max_length=MAX_STRING_LENGTH)
    contact_number = models.CharField(max_length=MAX_PHONE_LENGTH)
    address = models.CharField(max_length=MAX_ADDRESS_LENGTH)
    type = models.ForeignKey(TypeToChoose, on_delete=models.DO_NOTHING)
    basis = models.CharField(max_length=MAX_STRING_LENGTH)
    mail_address = models.CharField(max_length=MAX_ADDRESS_LENGTH)
    supreme_management_body = models.CharField(max_length=MAX_STRING_LENGTH)
    supervisor = models.CharField(max_length=MAX_STRING_LENGTH)
    supervisor_inn = models.CharField(max_length=INN_MAX_LENGTH)
    supervisory = models.CharField(max_length=MAX_STRING_LENGTH)
    collegiate_body = models.CharField(max_length=MAX_STRING_LENGTH)
    collegiate_person = models.CharField(max_length=MAX_STRING_LENGTH)
    employers_volume = models.IntegerField()
    salary_debt = models.IntegerField()
    company_group_name = models.CharField(max_length=MAX_STRING_LENGTH)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    group_members = models.JSONField(max_length=MAX_JSON_STRING_LENGTH)
    loan_amount = models.IntegerField()
    loan_time = models.IntegerField()
    loan_rate = models.FloatField()
    documents = models.ImageField( # это перепишем на много документов позже
        upload_to="documents",
        blank=True,
        null=True,
    )
    rate = models.CharField(max_length=MAX_STRING_LENGTH)
    tariff = models.ForeignKey(TariffPlan, on_delete=models.DO_NOTHING)
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
        return self.company_name


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


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        unique=True,
    )
    telegram_chat_id = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        unique=True,
    )
