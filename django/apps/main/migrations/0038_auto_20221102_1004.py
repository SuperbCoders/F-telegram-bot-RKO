# Generated by Django 3.1.1 on 2022-11-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20221102_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanrequest',
            name='telegram_chat_id',
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='is_finish',
            field=models.BooleanField(default=False),
        ),
    ]