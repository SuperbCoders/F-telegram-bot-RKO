# Generated by Django 3.1.1 on 2022-11-07 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20221107_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrequest',
            old_name='listCollegialExecutiveBody',
            new_name='list_collegial_executive_body',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='listSupervisotyBoardPersone',
            new_name='list_supervisoty_board_persone',
        ),
        migrations.RenameField(
            model_name='loanrequest',
            old_name='supervisotyBoardPersone_name',
            new_name='supervisoty_board_persone_name',
        ),
    ]
