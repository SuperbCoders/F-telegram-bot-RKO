# Generated by Django 3.1.1 on 2022-12-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_loanrequest_status_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='ogrn',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]