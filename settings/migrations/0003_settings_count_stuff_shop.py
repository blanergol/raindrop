# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-12 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_settings_sales_margin'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='count_stuff_shop',
            field=models.IntegerField(default=9, verbose_name='Количство товара в магазине'),
        ),
    ]