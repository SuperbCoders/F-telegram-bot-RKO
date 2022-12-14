# Generated by Django 3.1.1 on 2022-10-15 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20221014_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrequest',
            old_name='account_onw_role',
            new_name='account_operations',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='accownt_own_living',
            new_name='account_own_living',
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='account_own_role',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='assigned_publ_pers_registraion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='beneficiaries',
            field=models.BooleanField(default=bool),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='cash_source',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='division_code',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='operation_volume',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='outside_contracts_volume',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='state_employers',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='sum_per_month',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
    ]
