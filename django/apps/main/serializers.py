from rest_framework import serializers

from .models import (
    LoanApplication,
    LoanRequest,

)

class LoanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = [
                'id',
                'status',
                'inn',
                'company_name',
                'contact_number',
                
                'addresses',
                
                'supreme_management_body',
                'supreme_management_person',
                'supreme_management_inn',
                
                'supervisory_name',
                'supervisory_body',
                
                'collegiate_name',
                'collegiate_body',
                
                'account_onw_role',
                'account_own_lastname',
                'account_own_name',
                'account_own_surname',
                'account_own_gender',
                
                'account_onw_inn',
                'account_own_snils',
                'account_own_citizenship',
                'account_own_phone',
                'account_own_piece',
                
                'assigned_publ_pers_relation',
                'assigned_publ_pers_registraion', 
                'account_own_registration',
                
                'accownt_own_living',
                'account_own_mail',
                
                'first_passport_page',
                'account_birth_place',
                'account_datebirth',
                'doc_type',
                'doc_serial',
                'doc_number',
                'issued_by',
                'division_code',
                'date_issue',
                'validity',
                
                'foreigner_doc_type',
                'foreigner_doc_serial',
                'foreigner_doc_number',
                'foreigner_doc_issued',
                'foreigner_doc_validity',
                
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

                'tariff',
                'is_finished',
                'created_at',
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]
