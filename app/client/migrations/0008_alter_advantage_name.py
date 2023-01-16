# Generated by Django 3.2.16 on 2023-01-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_complex_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantage',
            name='name',
            field=models.CharField(choices=[('Security', 'Безопасность'), ('Layout', 'Планировка'), ('Interior', 'Внутренняя отделка'), ('Decoration', 'Концепция дома'), ('Infrastructure', 'Инфраструктура'), ('Location', 'Расположение'), ('Architecture', 'Архитектура'), ('Concierge', 'Консьерж сервис'), ('Parks', 'Парки'), ('Schools', 'Школы'), ('Entertainment', 'Театры и кино'), ('Hospitals', 'Больницы и мед центры')], max_length=180, verbose_name='Название'),
        ),
    ]