# Generated by Django 3.1.1 on 2022-11-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20221103_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='last_step',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
