# Generated by Django 5.0.6 on 2024-06-03 19:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
