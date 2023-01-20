# Generated by Django 3.2.16 on 2023-01-20 14:11

import ckeditor.fields
import client.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_alter_complex_ctype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=client.models.save_path, verbose_name='Фотография')),
                ('desciption', ckeditor.fields.RichTextField(blank=True, default='', max_length=200, verbose_name='Описание')),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.complex', verbose_name='Комплекс')),
            ],
            options={
                'verbose_name': 'Планировка',
                'verbose_name_plural': 'Планировки',
            },
        ),
    ]
