# Generated by Django 3.2.16 on 2023-01-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_complex_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complex',
            name='ctype',
            field=models.CharField(blank=True, help_text='Например: Клубный Дом, Жилой Комплекс и тд', max_length=180, null=True, verbose_name='Тип ЖК'),
        ),
    ]
