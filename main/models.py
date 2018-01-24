from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Video(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='Автор')
    title = models.CharField(verbose_name='Название', max_length=100, default='Название для видео')
    video_link = models.CharField(verbose_name='Ссылка на видео', max_length=200, default='http://youtube.com/')
    img = models.FileField(verbose_name='Картинка', default='st_img.png')
    img_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(380, 350)], format='JPEG', options={'quality': 100})
    created_date = models.DateField(verbose_name='Дата', default=timezone.now)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, default='Заголовок')
    text = RichTextField(verbose_name='Текст', default='Описание')
    img = models.FileField(verbose_name='Картинка', default='st_img.png')
    img_thumbnail = ImageSpecField(source='img', processors=[ResizeToFill(1550, 380)], format='JPEG', options={'quality': 100})

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.text


class Contact(models.Model):
    text = RichTextField(verbose_name='Текст', default='Описание')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.text
