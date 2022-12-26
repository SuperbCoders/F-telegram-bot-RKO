# Generated by Django 3.1.1 on 2022-12-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_auto_20221226_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrequest',
            old_name='list_collegial_executive_body',
            new_name='list_persone',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='collegiate_person',
            new_name='third_parties',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='is_collegiate_body',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='is_supervisoty',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='list_supervisoty_board_persone',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='supervisoty_board_persone_name',
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='informationGoals',
            field=models.JSONField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='planned_other',
            field=models.JSONField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='structure_value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='document_certifying_identity_executive',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='document_confirming_real_activity',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='document_licenses',
            field=models.JSONField(blank=True, null=True),
        ),
    ]