# Generated by Django 5.1.1 on 2024-11-14 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_regdoctors_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regdoctors',
            name='userId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.usermaster'),
        ),
    ]
