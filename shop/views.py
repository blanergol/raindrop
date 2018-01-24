from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.views import get_context_data
from users.models import Billing, Inventory, ShopStuffFavorites, ShopStuff
from lottery.models import Stuff, StuffAttributesType
from settings.models import Settings


def main(request):
    # обязательные данные
    context_data = get_context_data(request)

    settings = Settings.objects.first()
    all_stuff = Stuff.objects.filter(show_status=True).order_by('-id')
    all_stuff_count = all_stuff.count()
    paginator = Paginator(all_stuff, settings.count_stuff_shop)
    page = request.GET.get('page')
    try:
        all_stuff = paginator.page(page)
    except PageNotAnInteger:
        all_stuff = paginator.page(1)
    except EmptyPage:
        all_stuff = paginator.page(paginator.num_pages)

    stuff_attributes_type = StuffAttributesType.objects.all()

    # вывод данных в отображении
    context_data.update({'all_stuff': all_stuff, 'all_stuff_count': all_stuff_count, 'stuff_attributes_type': stuff_attributes_type})
    return render(request, 'shop/main.html', context_data)


def payment(request):
    if request.POST and request.is_ajax:
        stuff_id = request.POST.get('stuff_id')

        stuff = Stuff.objects.get(id=stuff_id, show_status=True, show_shop_status=True)
        user = User.objects.get(id=request.session['id'])
        billing = Billing.objects.get(user_id=user.id)

        if stuff.score < billing.score:
            Inventory.objects.create(user=user, stuff_id=stuff.id, type='shop')
            score = billing.score - stuff.score
            Stuff.objects.filter(id=stuff_id).update(show_status=False, show_shop_status=False)
            Billing.objects.filter(user_id=user.id).update(score=score)
            try:
                ShopStuffFavorites.objects.get(user=user, stuff=stuff).delete()
                message_response = {'status': 'success'}
            except ObjectDoesNotExist:
                message_response = {'status': 'success'}
        else:
            message_response = {'status': 'fail'}
        return HttpResponse(json.dumps(message_response))


def favorites(request):
    if request.POST and request.is_ajax():
        stuff_id = request.POST.get('stuff_id')

        user = User.objects.get(id=request.session['id'])
        try:
            stuff = Stuff.objects.get(id=stuff_id, show_status=True, show_shop_status=True)
            try:
                ShopStuffFavorites.objects.get(stuff=stuff)
            except ObjectDoesNotExist:
                ShopStuffFavorites.objects.create(user=user, stuff=stuff)
            message_response = {'status': 'success'}
        except ObjectDoesNotExist:
            message_response = {'status': 'fail'}
        return HttpResponse(json.dumps(message_response))


def favorites_remove(request):
    if request.POST and request.is_ajax():
        stuff_id = request.POST.get('stuff_id')

        user = User.objects.get(id=request.session['id'])
        try:
            stuff = Stuff.objects.get(id=stuff_id, show_status=True, show_shop_status=True)
            try:
                ShopStuffFavorites.objects.get(user=user, stuff=stuff).delete()
                message_response = {'status': 'success'}
            except ObjectDoesNotExist:
                message_response = {'status': 'fail'}
        except ObjectDoesNotExist:
            message_response = {'status': 'fail'}
        return HttpResponse(json.dumps(message_response))


def search(request):
    if request.POST:
        stuff_title = request.POST.get('stuff_title')

        # обязательные данные
        context_data = get_context_data(request)

        all_stuff = Stuff.objects.filter(title__search=stuff_title, show_shop_status=True, show_status=True)

        paginator = Paginator(all_stuff, 10)
        page = request.GET.get('page')
        try:
            all_stuff = paginator.page(page)
        except PageNotAnInteger:
            all_stuff = paginator.page(1)
        except EmptyPage:
            all_stuff = paginator.page(paginator.num_pages)

        stuff_attributes_type = StuffAttributesType.objects.all()

        # вывод данных в отображении
        context_data.update({'all_stuff': all_stuff, 'stuff_attributes_type': stuff_attributes_type})
        return render(request, 'shop/main.html', context_data)


def filter_price(request):
    if request.POST:
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')

        # обязательные данные
        context_data = get_context_data(request)

        all_stuff = Stuff.objects.filter(score__range=(min_price, max_price))

        paginator = Paginator(all_stuff, 10)
        page = request.GET.get('page')
        try:
            all_stuff = paginator.page(page)
        except PageNotAnInteger:
            all_stuff = paginator.page(1)
        except EmptyPage:
            all_stuff = paginator.page(paginator.num_pages)

        # вывод данных в отображении
        context_data.update({'all_stuff': all_stuff})
        return render(request, 'shop/main.html', context_data)


# продажа вещи купленной в магазине
def sell_stuff(request):
    if request.POST and request.is_ajax():
        stuff_id = request.POST.get('stuff_id')

        user = User.objects.get(id=request.session['id'])
        try:
            # поверяем на существование вещи
            stuff = Stuff.objects.get(id=stuff_id)
            try:
                # проверяем принадлжеит ли вещь пользователю
                Inventory.objects.get(stuff=stuff, user=user)
                # TODO:проценты за продажу вещи
                # переносим вещь в раздел продаж пользователя
                ShopStuff.objects.create(user=user, stuff=stuff)
                # удаляем вещь из аккаунта пользователя
                Inventory.objects.filter(user=user, stuff=stuff).delete()
                # размещаем вещь в магазине
                Stuff.objects.filter(id=stuff_id).update(show_shop_status=True, show_status=True)
                message_response = {'status': 'success'}
            except ObjectDoesNotExist:
                message_response = {'status': 'fail'}
        except ObjectDoesNotExist:
            message_response = {'status': 'fail'}
        return HttpResponse(json.dumps(message_response))


# снятие вещи с продажи
def remove_sell_stuff(request):
    if request.POST and request.is_ajax():
        stuff_id = request.POST.get('stuff_id')

        user = User.objects.get(id=request.session['id'])
        try:
            # проверяем существует ли вещь
            stuff = Stuff.objects.get(id=stuff_id)
            # снимаем с продажи
            Stuff.objects.filter(id=stuff_id).update(show_shop_status=False, show_status=False)
            # убираем вещь из раздела продаж пользователя
            ShopStuff.objects.get(stuff=stuff).delete()
            # возвращаем вещь на аккаут пользователя
            Inventory.objects.create(user=user, stuff=stuff)
            message_response = {'status': 'success'}
        except ObjectDoesNotExist:
            message_response = {'status': 'fail'}
        return HttpResponse(json.dumps(message_response))
