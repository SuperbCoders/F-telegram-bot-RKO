# Generated by Django 3.1.1 on 2022-12-28 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_auto_20221228_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrequest',
            old_name='certifying_identity_ceo',
            new_name='document_certifying_identity_ceo',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='document_certifying_identity_ceo_file',
        ),
    ]
