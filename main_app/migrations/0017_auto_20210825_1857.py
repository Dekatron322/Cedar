# Generated by Django 3.1.7 on 2021-08-25 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20210825_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresult',
            old_name='tt_exam',
            new_name='exams',
        ),
        migrations.RenameField(
            model_name='studentresult',
            old_name='tt_first_test',
            new_name='first',
        ),
        migrations.RenameField(
            model_name='studentresult',
            old_name='tt_second_test',
            new_name='second',
        ),
        migrations.RenameField(
            model_name='studentresult',
            old_name='tt_third_test',
            new_name='third',
        ),
    ]