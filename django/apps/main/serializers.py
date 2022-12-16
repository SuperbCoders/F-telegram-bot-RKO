from rest_framework import serializers

from .models import (
    LoanApplication,
    LoanRequest,
)


class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = [

            'short_name',
            'full_name',
            'registration_date',
            'kpp',
            'ogrn_date',
            'registrator_name',
            'okved',
            'oktmo',


            'id',
            'status',
            'status_description',
            'ogrn',
            'inn',
            'company_name',
            'contact_number',

            'addresses',

            'supreme_management_body',
            'supreme_management_person',
            'supreme_management_inn',

            'is_collegiate_body',
            'collegiate_person',
            'list_supervisoty_board_persone',

            'is_supervisoty',
            'supervisoty_board_persone_name',
            'list_collegial_executive_body',

            'licence_type',
            'licence_number',
            'licence_issued_by',
            'licence_date_issue',
            'licence_validity',
            'licenced_activity',

            'employers_volume',
            'salary_debt',

            'company_group_name',
            'start_date',
            'end_date',
            'group_members',

            'beneficiaries',

            'planned_operations',

            'account_operations',
            'operation_volume',
            'sum_per_month',
            'cash_source',
            'outside_contracts_volume',
            'state_employers',
            'information_goals',

            'tariff',
            'is_finished',
            'last_step',
            'created_at',
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]
