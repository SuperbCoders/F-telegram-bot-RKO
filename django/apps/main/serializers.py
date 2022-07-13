from rest_framework import serializers

from .models import (
    LoanApplication,
)


class LoanApplicationSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', required=False)

    class Meta:
        model = LoanApplication
        fields = [
            "id",
            "status",
            "loan_amount",
            "loan_term",
            "loan_region",
            "name",
            "city",
            "phone_number",
            "email",
            "old_name",
            "passport_photo_one",
            "passport_photo_two",
            "passport_photo_three",
            "passport_photo_four",
            "passport_photo_five",
            "passport_series",
            "passport_number",
            "passport_issue_date",
            "passport_code",
            "telegram_chat_id",
            "passport_issued_by",
            "passport_place_of_birth",
            "passport_date_of_birth",
            "old_passport_series",
            "old_passport_number",
            "old_passport_issue_date",
            "old_passport_code",
            "old_passport_issued_by",
            "old_passport_place_of_birth",
            "old_passport_date_of_birth",
            "current_address",
            "current_apartments_number",
            "has_no_current_address",
            "registration_address",
            "registration_apartments_number",
            "monthly_income",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "created_at",
        ]
