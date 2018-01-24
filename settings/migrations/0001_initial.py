# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-01 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Название сайта для поисковых систем', max_length=200, verbose_name='Название сайта')),
                ('description', models.TextField(default='Описание сайта для поисковых систем', max_length=500, verbose_name='Описаие сайта')),
                ('email', models.EmailField(default='info@raindrop.one', max_length=100, verbose_name='Основной Email')),
                ('short_description', models.TextField(default='Описание в подвал сайта', max_length=400, verbose_name='Краткое описание')),
                ('count_posts', models.IntegerField(default=6, verbose_name='Количество записей в блоге')),
                ('count_video', models.IntegerField(default=6, verbose_name='Количство видео')),
                ('vk_link', models.CharField(default='https://vk.com', max_length=100, verbose_name='Ссылка на vk')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]