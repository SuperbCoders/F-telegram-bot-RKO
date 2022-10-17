# Generated by Django 3.1.1 on 2022-10-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20221016_0750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrequest',
            old_name='passport_number',
            new_name='doc_number',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='passport_serial',
            new_name='doc_serial',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='supervisor_name',
            new_name='doc_type',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='supreme_management_type',
            new_name='supreme_management_person',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='basis',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='foreign_doc_number',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='foreign_doc_serial',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='foreign_doc_type',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='foreign_end',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='foreign_start',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='loan_amount',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='loan_rate',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='loan_time',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='rate',
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='account_onw_role',
            field=models.JSONField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='account_own_snils',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='beneficiaries',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='employers_volume',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='legal_address',
            field=models.JSONField(max_length=300),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='mail_address',
            field=models.JSONField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='physic_address',
            field=models.JSONField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
