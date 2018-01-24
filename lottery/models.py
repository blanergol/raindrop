from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class StuffAttributes(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, default='Название атрибута')

    class Meta:
        verbose_name = 'Атрибуты вещей'
        verbose_name_plural = 'Атрибуты вещей'

    def __str__(self):
        return self.title


class StuffAttributesType(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, default='Название типа атрибута')
    attributes = models.ManyToManyField(StuffAttributes, verbose_name='Атрибуты')

    class Meta:
        verbose_name = 'Типы атрибутов вещей'
        verbose_name_plural = 'Типы атрибутов вещей'

    def __str__(self):
        return self.title


class Stuff(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, default='Название вещей')
    attributes = models.ManyToManyField(StuffAttributes, verbose_name='Атрибуты')
    score = models.IntegerField(verbose_name='Стоимость', default=0)
    img = models.FileField(verbose_name='Картинка', default='st_img.png')
    img_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(300, 300)], format='PNG', options={'quality': 100})
    show_status = models.BooleanField(verbose_name='Участвует в розыгрыше', default=True)
    show_shop_status = models.BooleanField(verbose_name='Участвует в продаже', default=True)

    class Meta:
        verbose_name = 'Вещи'
        verbose_name_plural = 'Вещи'

    def __str__(self):
        return self.title


class Briefcases(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100, default='Название для кейса')
    type = models.CharField(verbose_name='Тип', max_length=100, default='#282840, #f92552')
    stuff = models.ManyToManyField(Stuff, verbose_name='Вещи')
    score = models.IntegerField(verbose_name='Стоимость', default=0)
    img = models.FileField(verbose_name='Картинка', default='st_img.png')
    img_thumbnail_main_page = ImageSpecField(source='img', processors=[ResizeToFill(400, 400)], format='PNG', options={'quality': 100})
    img_thumbnail_briefcases_page = ImageSpecField(source='img', processors=[ResizeToFill(300, 300)], format='PNG', options={'quality': 100})
    show_main_page_status = models.BooleanField(verbose_name='Отображать на лвной странице', default=True)
    created_date = models.DateField(verbose_name='Дата', default=timezone.now)

    class Meta:
        verbose_name = 'Кейсы'
        verbose_name_plural = 'Кейсы'

    def __str__(self):
        return self.title


class DotaboxModes(models.Model):
    title = models.CharField(verbose_name='Название режима', max_length=100, default='Название')
    description = models.TextField(verbose_name='Описание', default='Описание')
    stuff = models.ManyToManyField(Stuff, verbose_name='Вещи')
    score = models.IntegerField(verbose_name='Стоимость игры', default=0)
    enable = models.BooleanField(verbose_name='Режим включен', default=False)

    class Meta:
        verbose_name = 'Dota Box режимы'
        verbose_name_plural = 'Dota Box режимы'

    def __str__(self):
        return self.title
