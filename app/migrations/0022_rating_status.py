# Generated by Django 5.1.1 on 2024-11-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
