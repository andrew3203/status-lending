# Generated by Django 3.2.16 on 2023-01-16 06:44

import client.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advantage',
            name='image',
            field=models.ImageField(default=None, upload_to=client.models.save_path, verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
