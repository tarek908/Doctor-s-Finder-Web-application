# Generated by Django 5.1.1 on 2024-11-13 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='usreId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.usermaster'),
        ),
    ]
