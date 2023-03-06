from django.db import models
from django.contrib.sites.models import Site
from ckeditor.fields import RichTextField
import cyrtranslit
from django.utils.translation import gettext as _
import os


def save_path(instance, filename):
    filename = filename.replace(' ', '_')
    filename = cyrtranslit.to_latin(filename, 'ru').lower()
    return f'sites/{filename}'


class SiteData(models.Model):
    site = models.ForeignKey(
        Site,
        verbose_name=_('Сайт'),
        on_delete=models.CASCADE,
    )
    meta_title = models.CharField(
        _('Заголовок сайта'),
        help_text=_('Название сайта во вкладке'),
        max_length=80,
    )
    meta_description = models.TextField(
        _('Краткое описание (СЕО)'),
        help_text=_('Описание сайта (для ссылки) CEO'),
        max_length=500
    )
    scripts = models.TextField(
        _('Скрипты аналитики'),
        max_length=1500
    )
    created_at = models.DateTimeField(
        _('Создан'),
        auto_now_add=True
    )
    

    class Meta:
        verbose_name = _('Данные сайта')
        verbose_name_plural = _('Данные сайтов')

    def __str__(self) -> str:
        return f'{self.site.name}'


class Complex(models.Model):
    site =models.ForeignKey(
        SiteData,
        verbose_name=_('Сайт'),
        on_delete=models.SET_NULL, null=True
    )
    ctype = models.CharField(
        _('Тип ЖК'),
        help_text=_('Например: Клубный Дом, Жилой Комплекс и тд'),
        max_length=180, default="", blank=True
    )
    name = models.CharField(
        _('Название колмплекса'),
        max_length=180,
    )
    short = models.CharField(
        _('Краткое описание'),
        help_text=_('короткая фраза в начале страницы'),
        max_length=180,
    )
    slug = models.SlugField(
        _('Название страницы (латиницей)'),
        max_length=180
    )
    square = models.CharField(
        _('Доступная площядь'),
        help_text=_('Например: от 200 до 1500'),
        max_length=20,
    )
    phone = models.CharField(
        _('Контактный телефон'),
        max_length=20, null=True
    )
    title_phone = models.CharField(
        _('Контактный телефон (заголовок)'),
        max_length=20, null=True
    )
    price = models.IntegerField(
        _('Цена за м2'),
    )
    logo = models.FileField(
        _('Логотип'),
        upload_to=save_path, null=True
    )
    title_image = models.ImageField(
        _("Обложка"),
        help_text=_('Певрая фотография на странице'),
        upload_to=save_path,
    )
    presentation = models.FileField(
       _("Презентация проекта"),
        upload_to=save_path,
    )
    second_image = models.ImageField(
        _('Фото к описанию'),
        upload_to=save_path,
    )
    bg_image = models.ImageField(
        _('Фото на задний пдан формы'),
        upload_to=save_path, null=True
    )
    desciption = RichTextField(
        _('Описание'),
        max_length=900,
    )
    map = models.TextField(
        _('Скрипт карты'),
        max_length=1000,
    )
    is_published = models.BooleanField(
        _('Опубликован'),
        default=True, blank=True
    )
    private = models.BooleanField(
        _('Отобразить как отдельный сайт'),
        default=False, blank=True
    )

    wh_link = models.CharField(
        _('Ссылка WhatsApp'),
        max_length=580,
    )
    tg_link = models.CharField(
        _('Ссылка Telegramm'),
        max_length=580,
    )
    video_link = models.CharField(
        _('Ссылка на видео'),
        max_length=580, blank=True, default=None, null=True
    )

    created_at = models.DateTimeField(
        _('Создан'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Изменен'),
        auto_now=True
    )
    
    class Meta:
        verbose_name = _('Комплекс')
        verbose_name_plural = _('Комплексы')

    def __str__(self) -> str:
        return f'{self.name}'
    
    @property
    def formated_price(self):
        return '{:,}'.format(self.price).replace(',', ' ')
    
    @property
    def images(self):
        return Image.objects.filter(complex=self)
    
    @property
    def advantages(self):
        return Advantage.objects.filter(complex=self)
    
    @property
    def features(self):
        return Feature.objects.filter(complex=self)
    
    @property
    def layouts(self):
        return Layout.objects.filter(complex=self)
    
    @property
    def is_layouts(self):
        return len(self.layouts) > 0
    
    @property
    def is_video(self):
        return self.video_link is not None

    @property
    def video_key(self):
        if self.video_link:
            return self.video_link.rsplit('/', 1)[-1]
            

        

    formated_price.fget.short_description = _('Цена за м2')


class AdvantageType(models.TextChoices):
    SECURITY = 'Security', _('Безопасность')
    LAYOUT = 'Layout', _('Планировка')
    INTERIOR = 'Interior', _('Внутренняя отделка')
    DECORATION = 'Decoration', _('Концепция дома')
    INFRASTUCTURE = 'Infrastructure', _('Инфраструктура')
    LOCATION = 'Location', _('Расположение')
    ARCHITECTURE = 'Architecture', _('Архитектура')
    CONCIERGE = 'Concierge', _('Консьерж сервис')
    PARKS = 'Parks', _('Парки')
    SCHOOLS = 'Schools', _('Школы')
    ENTERTAIMENT = 'Entertainment', _('Театры и кино')
    HOSPITALS = 'Hospitals', _('Больницы и мед центры')


class Advantage(models.Model):
    name = models.CharField(
        _('Название'),
        choices=AdvantageType.choices,
        max_length=180,
    )
    desciption = RichTextField(
        _('Описание'),
        max_length=900,
    )
    image = models.ImageField(
        _("Фотография"),
        help_text=_('Фотография на задний фон'),
        upload_to=save_path,
    )
    complex =models.ForeignKey(
        Complex,
        verbose_name=_('Комплекс'),
        on_delete=models.CASCADE
    )

    @property
    def icon_path(self):
        return f'/static/utils/icons/icon_{self.name.lower()}.svg'
    
    class Meta:
        verbose_name = _('Приемущество')
        verbose_name_plural = _('Приемущества')

    def __str__(self) -> str:
        return f'{self.name}, {self.complex.name}'


class Feature(models.Model):
    name = models.CharField(
        _('Название'),
        help_text=_('Например: Апартаментов или Вилл'),
        max_length=180,
    )
    amount = models.IntegerField(
        _('Колличество'),
    )
    complex =models.ForeignKey(
        Complex,
        verbose_name=_('Комплекс'),
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = _('Особенность')
        verbose_name_plural = _('Особенности')

    def __str__(self) -> str:
        return f'{self.amount} {self.name}'


class Layout(models.Model):
    image = models.ImageField(
        _("Фотография"),
        upload_to=save_path,
    )
    complex =models.ForeignKey(
        Complex,
        verbose_name=_('Комплекс'),
        on_delete=models.CASCADE
    )
    desciption = models.TextField(
        _('Описание'),
        max_length=200,
        blank=True, default=''
    )
    
    class Meta:
        verbose_name = _('Планировка')
        verbose_name_plural = _('Планировки')

    def __str__(self) -> str:
        return f'{os.path.basename(self.image.name)}'


class Image(models.Model):
    image = models.ImageField(
        _("Фотография"),
        upload_to=save_path,
    )
    complex =models.ForeignKey(
        Complex,
        verbose_name=_('Комплекс'),
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = _('Фото')
        verbose_name_plural = _('Фотографии')

    def __str__(self) -> str:
        return f'{os.path.basename(self.image.name)}'

class Client(models.Model):

    site = models.ForeignKey(
        SiteData,
        verbose_name=_('Сайт'),
        on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(
        _('Имя'),
        max_length=32, null=True, blank=True
    )
    phone = models.CharField(
        _("Телефон"),
        max_length=20, null=True, blank=True
    )
    email = models.CharField(
       _("Почта"),
        max_length=32, null=True, blank=True
    )

    created_at = models.DateTimeField(
        _('Создан'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def __str__(self) -> str:
        return f'{self.name}'