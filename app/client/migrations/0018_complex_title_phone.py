# Generated by Django 3.2.18 on 2023-03-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0017_alter_complex_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='complex',
            name='title_phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Контактный телефон'),
        ),
    ]
