# Generated by Django 5.0.6 on 2024-06-17 18:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TTSAPI', '0002_transformationinfo_model_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformationinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transformationinfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
