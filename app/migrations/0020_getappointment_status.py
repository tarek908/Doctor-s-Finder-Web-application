# Generated by Django 5.1.1 on 2024-11-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_getappointment_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='getappointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]