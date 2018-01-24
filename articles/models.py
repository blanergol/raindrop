from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Articles(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='Автор')
    title = models.CharField(verbose_name='Заголовок', max_length=150)
    text = RichTextField(verbose_name='Текст статьи')
    created_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
    img = models.FileField(verbose_name='Картинка')
    img_thumbnail_short = ImageSpecField(source='img', processors=[ResizeToFill(380, 350)], format='JPEG', options={'quality': 100})
    img_thumbnail_full = ImageSpecField(source='img', processors=[ResizeToFill(774, 380)], format='JPEG', options={'quality': 100})
    comments_status = models.BooleanField(verbose_name='Отображать комментарии', default=False)
    views = models.IntegerField(verbose_name='Количество просмотров', default=0)

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
