# Generated by Django 3.1.1 on 2022-11-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20221102_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='inn',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
