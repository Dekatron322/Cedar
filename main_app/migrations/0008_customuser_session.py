# Generated by Django 3.1.7 on 2021-08-22 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210821_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.session'),
        ),
    ]