# Generated by Django 5.1.1 on 2024-11-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_getappointment_descrption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getappointment',
            name='usreId',
        ),
    ]