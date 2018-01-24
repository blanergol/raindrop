# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_settings_count_stuff_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='enable_dotabox',
            field=models.BooleanField(default=True, verbose_name='Режим DOTABOX включен'),
        ),
        migrations.AddField(
            model_name='settings',
            name='enable_magick_ball',
            field=models.BooleanField(default=True, verbose_name='Режим MAGICK BALL включен'),
        ),
        migrations.AddField(
            model_name='settings',
            name='enable_rdcase',
            field=models.BooleanField(default=True, verbose_name='Режим RDCASE включен'),
        ),
        migrations.AddField(
            model_name='settings',
            name='enable_techies',
            field=models.BooleanField(default=True, verbose_name='Режим TECHIES включен'),
        ),
    ]