# Generated by Django 3.1.1 on 2022-10-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20221016_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='account_operations',
            field=models.JSONField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='cash_source',
            field=models.JSONField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='planned_operations',
            field=models.JSONField(max_length=100),
        ),
    ]