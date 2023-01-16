# Generated by Django 3.2.16 on 2023-01-16 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20230116_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='complex',
            name='ctype',
            field=models.CharField(default='', help_text='Например: Клубный Дом, Жилой Комплекс и тд', max_length=180, verbose_name='Тип ЖК'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complex',
            name='short',
            field=models.CharField(default='', help_text='короткая фраза в начале страницы', max_length=180, verbose_name='Краткое описание'),
            preserve_default=False,
        ),
    ]