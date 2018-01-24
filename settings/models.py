from django.db import models


class Settings(models.Model):
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    title = models.CharField(verbose_name='Название сайта', max_length=200, default='Название сайта для поисковых систем')
    description = models.TextField(verbose_name='Описаие сайта', max_length=500, default='Описание сайта для поисковых систем')
    email = models.EmailField(verbose_name='Основной Email', max_length=100, default='info@raindrop.one')
    short_description = models.TextField(verbose_name='Краткое описание', max_length=400, default='Описание в подвал сайта')
    count_posts = models.IntegerField(verbose_name='Количество записей в блоге', default=6)
    count_video = models.IntegerField(verbose_name='Количство видео', default=6)
    count_stuff_shop = models.IntegerField(verbose_name='Количство товара в магазине', default=9)
    vk_link = models.CharField(verbose_name='Ссылка на vk', max_length=100, default='https://vk.com')
    sales_margin = models.IntegerField(verbose_name='Наценка на продажу вещи (%)', default=10)
    enable_rdcase = models.BooleanField(verbose_name='Режим RDCASE включен', default=True)
    enable_dotabox = models.BooleanField(verbose_name='Режим DOTABOX включен', default=True)
    enable_magick_ball = models.BooleanField(verbose_name='Режим MAGICK BALL включен', default=True)
    enable_techies = models.BooleanField(verbose_name='Режим TECHIES включен', default=True)
    enable_shop = models.BooleanField(verbose_name='Магазин включен', default=True)

    def __str__(self):
        return self.title
