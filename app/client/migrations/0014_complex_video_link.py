# Generated by Django 3.2.16 on 2023-01-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_alter_layout_desciption'),
    ]

    operations = [
        migrations.AddField(
            model_name='complex',
            name='video_link',
            field=models.CharField(blank=True, default=None, max_length=580, null=True, verbose_name='Ссылка на видео'),
        ),
    ]
