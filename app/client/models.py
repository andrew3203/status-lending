from django.db import models
from django.contrib.sites.models import Site
from ckeditor.fields import RichTextField
import cyrtranslit
import os


def save_path(instance, filename):
    filename = filename.replace(' ', '_')
    filename = cyrtranslit.to_latin(filename, 'ru').lower()
    return f'sites/{filename}'


class SiteData(models.Model):
    site = models.ForeignKey(
        Site,
        verbose_name='Сайт',
        on_delete=models.CASCADE,
    )
    meta_title = models.CharField(
        'Заголовок сайта',
        help_text='Название сайта во вкладке',
        max_length=80,
    )
    meta_description = models.TextField(
        'Краткое описание (СЕО)',
        help_text='Описание сайта (для ссылки) CEO',
        max_length=500
    )
    scripts = models.TextField(
        'Скрипты аналитики',
        max_length=1500
    )
    created_at = models.DateTimeField(
        'Создан',
        auto_now_add=True
    )
    

    class Meta:
        verbose_name = 'Данные сайта'
        verbose_name_plural = 'Данные сайтов'

    def __str__(self) -> str:
        return f'{self.site.name}'


class Complex(models.Model):
    site =models.ForeignKey(
        Site,
        verbose_name='Сайт',
        on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(
        'Название колмплекса',
        max_length=180,
    )
    square = models.CharField(
        'Доступная площядь',
        help_text='Например: от 200 до 1500',
        max_length=20,
    )
    price = models.FloatField(
        'Цена за м2',
    )
    title_image = models.ImageField(
        "Обложка",
        help_text='Певрая фотография на странице',
        upload_to=save_path,
    )
    presentation = models.FileField(
        "Презентация проекта",
        upload_to=save_path,
    )
    second_image = models.ImageField(
        'Фото к описанию',
        upload_to=save_path,
    )
    desciption = RichTextField(
        'Описание',
        max_length=900,
    )
    map = models.TextField(
        'Скрипт карты',
        max_length=1000,
    )
    is_published = models.BooleanField(
        'Опубликован',
        default=True, blank=True
    )

    wh_link = models.CharField(
        'Ссылка WhatsApp',
        max_length=580,
    )
    tg_link = models.CharField(
        'Ссылка Telegramm',
        max_length=580,
    )

    created_at = models.DateTimeField(
        'Создан',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Изменен',
        auto_now=True
    )
    
    class Meta:
        verbose_name = 'Комплекс'
        verbose_name_plural = 'Комплексы'

    def __str__(self) -> str:
        return f'{self.name}'


class AdvantageType(models.TextChoices):
    SECURITY = 'Security', 'Безопасность'
    LAYOUT = 'Layout', 'Планировка'
    INTERIOR = 'Interior', 'Внутренняя отделка'
    CONCEPT = 'Concept', 'Концепция дома'
    INFRASTUCTURE = 'Infrastructure', 'Инфраструктура'
    LOCATION = 'Location', 'Расположение'
    ARCHITECTURE = 'Architecture', 'Архитектура'
    CONCIERGE = 'Concierge', 'Консьерж сервис'
    PARKS = 'Parks', 'Парки'
    SCHOOLS = 'Schools', 'Школы'
    ENTERTAIMENT = 'Entertainment', 'Театры и кино'
    HOSPITALS = 'Hospitals', 'Больницы и мед центры'


class Advantage(models.Model):
    name = models.CharField(
        'Название',
        choices=AdvantageType.choices,
        max_length=180,
    )
    desciption = RichTextField(
        'Описание',
        max_length=900,
    )
    complex =models.ForeignKey(
        Complex,
        verbose_name='Комплекс',
        on_delete=models.CASCADE
    )

    @property
    def image_path(self):
        return f'/static/utils/icons/icon_{self.name.lower()}.svg'
    
    class Meta:
        verbose_name = 'Приемущество'
        verbose_name_plural = 'Приемущества'

    def __str__(self) -> str:
        return f'{self.name}, {self.complex.name}'


class Feature(models.Model):
    name = models.CharField(
        'Название',
        help_text='Например: Апартаментов или Вилл',
        max_length=180,
    )
    amount = models.IntegerField(
        'Колличество',
    )
    complex =models.ForeignKey(
        Complex,
        verbose_name='Комплекс',
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'

    def __str__(self) -> str:
        return f'{self.amount} {self.name}'


class Image(models.Model):
    image = models.ImageField(
        "Фотография",
        upload_to=save_path,
    )
    complex =models.ForeignKey(
        Complex,
        verbose_name='Комплекс',
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self) -> str:
        return f'{os.path.basename(self.image.name)}'

class Client(models.Model):

    site =models.ForeignKey(
        Site,
        verbose_name='Сайт',
        on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(
        'Имя',
        max_length=32, null=True, blank=True
    )
    phone = models.CharField(
        "Телефон",
        max_length=20, null=True, blank=True
    )
    email = models.CharField(
        "Почта",
        max_length=32, null=True, blank=True
    )

    created_at = models.DateTimeField(
        'Создан',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self) -> str:
        return f'{self.name}'