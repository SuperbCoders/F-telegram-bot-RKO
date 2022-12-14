# Generated by Django 3.1.1 on 2022-10-14 09:57

from datetime import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20221014_0538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrequest',
            old_name='collegiate_person',
            new_name='account_birth_place',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='supervisor',
            new_name='account_datebirth',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='type',
            new_name='account_onw_inn',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='real_mail_address',
            new_name='mail_address',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='supervisor_inn',
            new_name='supreme_management_inn',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='legal_mail_address',
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_onw_role',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_citizenship',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_gender',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_lastname',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_mail',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_name',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_phone',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_piece',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_registration',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_snils',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_surname',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='accownt_own_living',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='assigned_publ_pers_relation',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='collegiate_person_fio',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='date_issue',
            field=models.DateField(default=datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='first_passport_page',
            field=models.ImageField(default=str, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='foreign_doc_number',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='foreign_doc_serial',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='foreign_doc_type',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='foreign_end',
            field=models.DateField(default=datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='foreign_start',
            field=models.DateField(default=datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='issued_by',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='licence_date_issue',
            field=models.DateField(default=datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='licence_issued_by',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='licence_number',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='licence_type',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='licence_validity',
            field=models.DateField(default=datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='licenced_activity',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='passport_number',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='passport_serial',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='planned_operations',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='supervisor_name',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='supreme_management_type',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='validity',
            field=models.DateField(default=datetime.now()),
            preserve_default=False,
        ),
    ]
