# Generated by Django 3.1.7 on 2021-08-21 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210714_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresult',
            name='class_average',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='highest_in_class',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='lowest_in_class',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='position',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='total',
        ),
    ]
