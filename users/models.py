from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from lottery.models import Stuff


class Service(models.Model):
    user = models.OneToOneField(User)
    exchange_link = models.CharField(verbose_name='Ссылка на обен', max_length=100, default='')

    class Meta:
        verbose_name = 'Доп. инф. о пользователях'
        verbose_name_plural = 'Доп. инф. о пользователях'

    def __str__(self):
        return self.user.username


class Inventory(models.Model):
    user = models.ForeignKey(User)
    stuff = models.OneToOneField('lottery.Stuff', verbose_name='Вещь')
    type = models.CharField(verbose_name='Способ получения вещи', default='games', max_length=20)

    class Meta:
        verbose_name = 'Вещи'
        verbose_name_plural = 'Вещи'

    def __str__(self):
        return self.stuff.title


class HistoryGames(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', default=1)
    type = models.CharField(verbose_name='Тип игры', max_length=100, default='rdcase')
    stuff = models.OneToOneField(Stuff, verbose_name='Вещь', default=1)
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now)

    class Meta:
        verbose_name = 'История игр'
        verbose_name_plural = 'История игр'

    def __str__(self):
        return self.user.username


class Billing(models.Model):
    user = models.OneToOneField(User)
    money = models.IntegerField(verbose_name='Количество денег внесено', default=0)
    score = models.IntegerField(verbose_name='Количество монет', default=0)
    coins = models.IntegerField(verbose_name='Монеты', default=0)

    class Meta:
        verbose_name = 'Счета'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return self.user.username


class BillingHistory(models.Model):
    user = models.ForeignKey(User)
    money = models.IntegerField(verbose_name='Внесено в денежном эквиваленте', default=0)
    score = models.IntegerField(verbose_name='Внесено монет', default=0)
    payment_status = models.CharField(verbose_name='Статус платежа', default='proccess', max_length=100)
    date = models.DateField(verbose_name='Дата', default=timezone.now)

    class Meta:
        verbose_name = 'История пополнения'
        verbose_name_plural = 'История пополнения'

    def __str__(self):
        return self.user.username


class ShopStuff(models.Model):
    user = models.ForeignKey(User)
    stuff = models.OneToOneField(Stuff, verbose_name='Вещь', default=1)

    class Meta:
        verbose_name = 'Вещи на продажу'
        verbose_name_plural = 'Вещи на продажу'

    def __str__(self):
        return self.user.username


class ShopStuffFavorites(models.Model):
    user = models.ForeignKey(User)
    stuff = models.OneToOneField(Stuff, verbose_name='Вещь', default=1)

    class Meta:
        verbose_name = 'Избранные вещи'
        verbose_name_plural = 'Избранные вещи'

    def __str__(self):
        return self.user.username
