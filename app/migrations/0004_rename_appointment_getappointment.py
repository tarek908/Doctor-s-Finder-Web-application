# Generated by Django 5.1.1 on 2024-11-13 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_appointment_usreid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='appointment',
            new_name='getAppointment',
        ),
    ]