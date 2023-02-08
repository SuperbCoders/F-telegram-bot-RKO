from rest_framework import serializers

from .models import (
    LoanApplication,
    LoanRequest,
)


class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = [

            'short',
            'full_name',
            'registration_date',
            'kpp',
            'ogrn_date',
            'registrator_name',
            'okved',
            'oktmo',

            'email',
            'donainname',
            'fax',
            'founders',
            'information_counterparties',
            'name_organization',
            'information_counterparties_two',
            'name_organization_two',
            'codeword',
            'sms_sending',
            'is_conditions',
            'additional_products',
            'opf',


            'subject_licensing',
            'history_reputation',
            'num_transactions_month',
            'num_transactions_week',
            'num_transactions_quarter',
            'num_transactions_age',
            'sum_transactions_month',
            'sum_transactions_week',
            'sum_transactions_quarter',
            'sum_transactions_age',


            'monthly_cash_withdrawal',
            'week_cash_withdrawal',


            'quarter_cash_withdrawal',
            'age_cash_withdrawal',


            'sum_mouth_cash_withdrawal',
            'sum_week_cash_withdrawal',
            'sum_quarter_cash_withdrawal',
            'sum_age_cash_withdrawal',

            'foreign_trade_contracts_month',
            'foreign_trade_contracts_week',
            'foreign_trade_contracts_quarter',
            'foreign_trade_contracts_age',
            'foreign_sum_contracts_month',
            'foreign_sum_contracts_week',
            'foreign_sum_contracts_quarter',
            'foreign_sum_contracts_age',
            'sources_cash_receipts',
            'headcount',


            'document_certifying_identity_executive',
            'document_confirming_real_activity',
            'document_licenses',


            'structure_value',


            'id',
            'status',
            'status_description',
            'order_id',
            'ogrn',
            'inn',
            'company_name',
            'contact_number',

            'addresses',

            'supreme_management_body',
            'supreme_management_person',
            'supreme_management_inn',

            'list_persone',

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
