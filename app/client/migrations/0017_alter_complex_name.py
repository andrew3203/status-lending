# Generated by Django 3.2.17 on 2023-02-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0016_auto_20230206_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complex',
            name='name',
            field=models.CharField(max_length=180, verbose_name='Complex Name'),
        ),
    ]
