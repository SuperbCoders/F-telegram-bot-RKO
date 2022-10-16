from rest_framework import serializers

from .models import (
    LoanApplication,
    LoanRequest,

)

class LoanRequestSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', required=False)
    class Meta:
        model = LoanRequest
        fields = [
            "id",
            "status",
            
            "inn",
            "company_name",
            "contact_number",
            
            "legal_address",
            "physic_address",
            "mail_address",

            "supreme_management_body",
            "supreme_management_person",
            "supreme_management_inn",
            "supervisory",
            "collegiate_body",
            "collegiate_person_fio",

            "account_onw_role",
            "account_own_lastname",
            "account_own_name",
            "account_own_surname",
            "account_own_gender",
            "account_onw_inn",
            "account_own_snils",
            "account_own_citizenship",
            "account_own_phone",
            "account_own_piece",
            
            "assigned_publ_pers_relation",
            "account_own_registration",
            
            "accownt_own_living",
            "account_own_mail",
            
            "first_passport_page",
            "account_birth_place",
            "account_datebirth",
            "doc_type",
            "doc_serial",
            "doc_number",
            "issued_by",
            "date_issue",
            "validity",

            "licence_type",
            "licence_number",
            "licence_issued_by",
            "licence_date_issue",
            "licence_validity",
            "licenced_activity",

            "employers_volume",
            "salary_debt",

            "company_group_name",
            "start_date",
            "end_date",
            "group_members",
            
            "first_passport_page",
            "telegram_chat_id",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "created_at",
        ]


# class LoanApplicationSerializer(serializers.ModelSerializer):
#     status = serializers.CharField(source='get_status_display', required=False)

#     class Meta:
#         model = LoanApplication
#         fields = [
#             "id",
#             "status",
#             "loan_amount",
#             "loan_term",
#             "loan_region",
#             "name",
#             "city",
#             "phone_number",
#             "email",
#             "old_name",
#             "passport_photo_one",
#             "passport_photo_two",
#             "passport_photo_three",
#             "passport_photo_four",
#             "passport_photo_five",
#             "passport_series",
#             "passport_number",
#             "passport_issue_date",
#             "passport_code",
#             "telegram_chat_id",
#             "passport_issued_by",
#             "passport_place_of_birth",
#             "passport_date_of_birth",
#             "old_passport_series",
#             "old_passport_number",
#             "old_passport_issue_date",
#             "old_passport_code",
#             "old_passport_issued_by",
#             "old_passport_place_of_birth",
#             "old_passport_date_of_birth",
#             "current_address",
#             "current_apartments_number",
#             "has_no_current_address",
#             "registration_address",
#             "registration_apartments_number",
#             "monthly_income",
#             "created_at",
#         ]
#         read_only_fields = [
#             "id",
#             "status",
#             "created_at",
#         ]
