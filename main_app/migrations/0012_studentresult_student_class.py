# Generated by Django 3.1.7 on 2021-08-24 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_student_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.course'),
        ),
    ]
