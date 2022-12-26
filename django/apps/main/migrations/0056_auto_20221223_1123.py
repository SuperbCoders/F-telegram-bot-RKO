# Generated by Django 3.1.1 on 2022-12-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_auto_20221223_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='num_transactions_age',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='sum_age_cash_withdrawal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='sum_mouth_cash_withdrawal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='sum_quarter_cash_withdrawal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='sum_transactions_week',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='sum_week_cash_withdrawal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]