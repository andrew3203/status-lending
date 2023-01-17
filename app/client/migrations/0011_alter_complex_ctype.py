# Generated by Django 3.2.16 on 2023-01-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_alter_complex_ctype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complex',
            name='ctype',
            field=models.CharField(blank=True, default='', help_text='Например: Клубный Дом, Жилой Комплекс и тд', max_length=180, verbose_name='Тип ЖК'),
        ),
    ]
