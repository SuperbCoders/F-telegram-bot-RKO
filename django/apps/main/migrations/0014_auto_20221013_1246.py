# Generated by Django 3.1.1 on 2022-10-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20221013_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='physic_address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='real_mail_address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='tariff',
            field=models.CharField(max_length=100),
        ),
    ]
