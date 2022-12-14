# Generated by Django 3.1.1 on 2022-10-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20221013_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('under_review', 'На рассмотрении'), ('declined', 'Отклонена'), ('approved', 'Одобрена'), ('update', 'Доработка заявки')], default='under_review', max_length=140),
        ),
    ]
