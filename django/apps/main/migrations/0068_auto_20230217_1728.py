# Generated by Django 3.1.1 on 2023-02-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0067_auto_20230215_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrequest',
            name='last_status',
            field=models.CharField(blank=True, default='under_review', max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='status',
            field=models.CharField(blank=True, default='under_review', max_length=140, null=True),
        ),
    ]
