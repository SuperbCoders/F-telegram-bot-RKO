from pyexpat import model
import random
from re import S
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
        ("update", "Доработка заявки")
    ]
    status = models.CharField(max_length=140,
                              choices=STATUS_CHOICES,
                              default="under_review",
                              blank=True)
    last_status = models.CharField(max_length=140,
                              choices=STATUS_CHOICES,
                              default="under_review",
                              blank=True)
    inn = models.CharField(max_length=INN_MAX_LENGTH)
    company_name = models.CharField(max_length=MAX_STRING_LENGTH)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    
    addresses = models.JSONField(max_length=300)
    # basis = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    
    supreme_management_body = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    supreme_management_person = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    supreme_management_inn = models.CharField(max_length=INN_MAX_LENGTH, blank=True, null=True)
    
    supervisory = models.JSONField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    
    collegiate_body = models.JSONField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    
    account_onw_role = models.JSONField(max_length=MAX_JSON_STRING_LENGTH, blank=True, null=True)
    account_own_lastname =models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    account_own_name = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    account_own_surname = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    account_own_gender = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    
    account_onw_inn = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    account_own_snils = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    account_own_citizenship = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    account_own_phone = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    account_own_piece = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    
    assigned_publ_pers_relation = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    assigned_publ_pers_registraion = models.CharField(max_length=MAX_STRING_LENGTH, blank = True, null=True)
    account_own_registration = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    
    accownt_own_living = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    account_own_mail = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    
    first_passport_page = models.ImageField(
        upload_to="documents",
        blank=True,
        null=True,)
    account_birth_place = models.CharField(max_length=MAX_STRING_LENGTH)
    account_datebirth = models.CharField(max_length=MAX_STRING_LENGTH)
    doc_type = models.CharField(max_length=MAX_STRING_LENGTH)
    doc_serial = models.CharField(max_length=MAX_STRING_LENGTH)
    doc_number = models.CharField(max_length=MAX_STRING_LENGTH)
    issued_by = models.CharField(max_length=MAX_STRING_LENGTH)
    division_code = models.CharField(max_length=MAX_STRING_LENGTH)
    date_issue = models.DateField()
    validity = models.DateField()

    licence_type = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    licence_number = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    licence_issued_by = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    licence_date_issue = models.DateField(blank=True, null=True)
    licence_validity = models.DateField(blank=True, null=True)
    licenced_activity = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)

    employers_volume = models.CharField(max_length=MAX_STRING_LENGTH)
    salary_debt = models.BigIntegerField()

    company_group_name = models.CharField(max_length=MAX_STRING_LENGTH)
    start_date = models.DateField()
    end_date = models.DateField()
    group_members = models.JSONField(max_length=MAX_JSON_STRING_LENGTH)
    
    beneficiaries = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    
    planned_operations = models.JSONField(max_length=MAX_STRING_LENGTH)
    
    account_operations = models.JSONField(max_length=MAX_STRING_LENGTH)
    operation_volume = models.CharField(max_length=MAX_STRING_LENGTH)
    sum_per_month = models.CharField(max_length=MAX_STRING_LENGTH)
    cash_source = models.JSONField(max_length=MAX_STRING_LENGTH)
    outside_contracts_volume = models.CharField(max_length=MAX_STRING_LENGTH)
    state_employers = models.CharField(max_length=MAX_STRING_LENGTH)

    # rate = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    tariff = models.CharField(max_length=MAX_STRING_LENGTH)
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

    def _send_change_status_message_to_telegram(self):
        print(self)
        print("Пошла отправка")
        if self.status == "update": 
            print(self.status)
            text = (
                f"{self.account_own_name} {self.account_own_lastname}, нам необходима дополнительная"
                + "информация по вашей заявке на открытие счёта."
                + "Подробнее — в мобильном и интернет-банке: ДИПЛИНК"
            )
            button_text = "Перейти в мобильный банк"
            button_url = "https://www.yandex.ru/"
            send_telegram_bot_message.delay(
                self.telegram_chat_id,
                text,
                button_url=button_url,
                button_text=button_text,
                delay=1,
            )
            self.last_status = self.status
        elif self.status == "declined":
            print(self.status)
            text = (
                f"{self.account_own_name} {self.account_own_lastname}, к сожалению,"
                + "заявка на открытие счёта отменена банком. Контакты кц"
            )
            button_text = "Контактный центр"
            button_url = "https://www.yandex.ru/"
            send_telegram_bot_message.delay(
                self.telegram_chat_id,
                text,
                button_url=button_url,
                button_text=button_text,
                delay=1,
            )
            self.last_status = self.status

        elif self.status == "approved":
            print(self.status)
            print(self.company_name)
            text = ''
            print(self.company_name.find('ИП '))
            if self.company_name.find('ИП ') != -1:
                print("чел ип")
                text = (
                    f"{self.account_own_name} {self.account_own_lastname}," 
                    + "вам одобрено открытие расчётного счёта. В ближайшее время мы позвоним,"
                    + "чтобы назначить встречу с представителем банка. Конакты КЦ"
                )
            elif self.company_name.find('ООО ') !=-1:
                print("Чел ООО")
                text = (
                    f"{self.account_own_name} {self.account_own_lastname}," 
                    + f"для {self.company_name} одобрено открытие расчётного счёта." 
                    +"В ближайшее время мы позвоним, чтобы назначить встречу с представителем банка.  Конакты КЦ" 
                )
            button_text = "Контактный центр"
            button_url = "https://www.yandex.ru/"
            send_telegram_bot_message.delay(
                self.telegram_chat_id,
                text,
                button_url=button_url,
                button_text=button_text,
                delay=1,
            )
            self.last_status = self.status
        elif self.status == "under_review":
            
            text = (
                f"{self.account_own_name} {self.account_own_lastname}," 
                +"Ваша заявка на открытие счёта находится на рассмотрении." 
                +"Подробнее — в мобильном и интернет-банке: ДИПЛИНК"
            )
            print(text)
            button_text = "Контактный центр"
            button_url = "https://www.yandex.ru/"
            send_telegram_bot_message.delay(
                self.telegram_chat_id,
                text,
                button_url=button_url,
                button_text=button_text,
                delay=1,
            )
            self.last_status = self.status
    class Meta:
        verbose_name = 'заявление'
        verbose_name_plural = "заявления"

    def save(self, *args, **kwargs):
        print(self.status)
        print(self.last_status)
        print(args)
        print(kwargs)
        if not self.pk and self.status == self.last_status:
            self._send_success_message_to_telegram()
            self._send_upload_message_to_telegram()
        elif self.status != self.last_status:
            print("Пошел апдейт")
            self._send_change_status_message_to_telegram()
        super().save(*args, **kwargs)


    # def update

    def __str__(self):
        return self.company_name


class LoanApplication(models.Model):
    STATUS_CHOICES = [
        ("under_review", "На рассмотрении"),
        ("declined", "Отклонена"),
        ("approved", "Одобрена"),
        ("update", "Доработка заявки")
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
