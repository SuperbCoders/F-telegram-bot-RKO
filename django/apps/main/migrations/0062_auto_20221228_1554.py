# Generated by Django 3.1.1 on 2022-12-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_auto_20221228_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='certifying_identity_ceo',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='document_certifying_identity_ceo_file',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
