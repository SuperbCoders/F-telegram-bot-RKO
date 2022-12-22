# Generated by Django 3.1.1 on 2022-12-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_auto_20221216_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.DeleteModel(
            name='PassportFile',
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='donainname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='fax',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='founders',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='information_counterparties',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='information_counterparties2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='name_organization',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='name_organization2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='planning',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='sms_sending',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]