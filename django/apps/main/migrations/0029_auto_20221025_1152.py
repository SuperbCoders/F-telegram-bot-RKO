# Generated by Django 3.1.1 on 2022-10-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20221025_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='date_issue',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='validity',
            field=models.DateField(blank=True, null=True),
        ),
    ]
