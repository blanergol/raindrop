from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
import json

from main.views import get_context_data
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .models import Billing, BillingHistory, HistoryGames, Inventory, Service, ShopStuff, ShopStuffFavorites


# проверка авторизации
def check_auth(request, pk):
    if 'id' in request.session:
        if int(request.session['id']) == int(pk):
            return True
        else:
            return HttpResponseRedirect(reverse('users:profile', args=(str(request.session['id']))))
    else:
        return HttpResponseRedirect(reverse('main:main'))


# профиль пользователя
def profile(request, pk):
    # проверка авторизации
    auth = check_auth(request, pk)
    if auth == True:
        # обязательные данные
        context_data = get_context_data(request)

        user = get_object_or_404(User, pk=pk)

        # вывод данных в отображении
        context_data.update({'user': user})
        return render(request, 'users/profile.html', context_data)
    else:
        return auth


# история игр
def history_games(request, pk):
    # проверка авторизации
    auth = check_auth(request, pk)
    if auth == True:
        # обязательные данные
        context_data = get_context_data(request)

        user = get_object_or_404(User, pk=pk)

        # получение истории игр
        history_games = HistoryGames.objects.filter(user=user)
        paginator = Paginator(history_games, 5)
        page = request.GET.get('page_history_games')
        try:
            history_games = paginator.page(page)
        except PageNotAnInteger:
            history_games = paginator.page(1)
        except EmptyPage:
            history_games = paginator.page(paginator.num_pages)

        # вывод данных в отображении
        context_data.update({'user': user, 'history_games': history_games})
        return render(request, 'users/history_games.html', context_data)
    else:
        return auth


# биллинг
def billing(request, pk):
    # проверка авторизации
    auth = check_auth(request, pk)
    if auth == True:
        # обязательные данные
        context_data = get_context_data(request)

        user = get_object_or_404(User, pk=pk)
        # получение биллиноговой информации пользователя
        billing_history = BillingHistory.objects.all().filter(user=user)
        paginator = Paginator(billing_history, 5)
        page = request.GET.get('page_billing_history')
        try:
            billing_history = paginator.page(page)
        except PageNotAnInteger:
            billing_history = paginator.page(1)
        except EmptyPage:
            billing_history = paginator.page(paginator.num_pages)

        # вывод данных в отображении
        context_data.update({'billing_history': billing_history})
        return render(request, 'users/billing.html', context_data)
    else:
        return auth


# инвентарь
def inventory(request, pk):
    # проверка авторизации
    auth = check_auth(request, pk)
    if auth == True:
        # обязательные данные
        context_data = get_context_data(request)

        user = get_object_or_404(User, pk=pk)

        # получение всех вещей пользователя
        inventory = Inventory.objects.filter(user=user)

        # получение выигранных вещей пользователя
        inventory_games = inventory.filter(type='games')
        paginator = Paginator(inventory_games, 5)
        page = request.GET.get('page_inventory_games')
        try:
            inventory_games = paginator.page(page)
        except PageNotAnInteger:
            inventory_games = paginator.page(1)
        except EmptyPage:
            inventory_games = paginator.page(paginator.num_pages)

        # получение купленных вещей пользователя
        inventory_shop = inventory.filter(type='shop')
        paginator = Paginator(inventory_shop, 5)
        page = request.GET.get('page_inventory_shop')
        try:
            inventory_shop = paginator.page(page)
        except PageNotAnInteger:
            inventory_shop = paginator.page(1)
        except EmptyPage:
            inventory_shop = paginator.page(paginator.num_pages)

        # получение вещей из стима пользователя
        inventory_steam = inventory.filter(type='steam')
        paginator = Paginator(inventory_steam, 5)
        page = request.GET.get('page_inventory_steam')
        try:
            inventory_steam = paginator.page(page)
        except PageNotAnInteger:
            inventory_steam = paginator.page(1)
        except EmptyPage:
            inventory_steam = paginator.page(paginator.num_pages)

        user_service = Service.objects.get(user=user)

        # вывод данных в отображении
        context_data.update({'user': user, 'user_service': user_service, 'inventory_games': inventory_games, 'inventory_shop': inventory_shop,
                             'inventory_steam': inventory_steam})
        return render(request, 'users/inventory.html', context_data)
    else:
        return auth


# магазин
def shop(request, pk):
    # проверка авторизации
    auth = check_auth(request, pk)
    if auth == True:
        # обязательные данные
        context_data = get_context_data(request)

        user = get_object_or_404(User, pk=pk)

        # получение вещей находящихся на продажи в магазине
        shop_stuff = ShopStuff.objects.filter(user=user)
        paginator = Paginator(shop_stuff, 5)
        page = request.GET.get('page_shop_stuff')
        try:
            shop_stuff = paginator.page(page)
        except PageNotAnInteger:
            shop_stuff = paginator.page(1)
        except EmptyPage:
            shop_stuff = paginator.page(paginator.num_pages)

        # получение избранных вещей
        shop_stuff_favorites = ShopStuffFavorites.objects.filter(user=user)
        paginator = Paginator(shop_stuff_favorites, 5)
        page = request.GET.get('page_stuff_fav')
        try:
            shop_stuff_favorites = paginator.page(page)
        except PageNotAnInteger:
            shop_stuff_favorites = paginator.page(1)
        except EmptyPage:
            shop_stuff_favorites = paginator.page(paginator.num_pages)

        user_service = Service.objects.get(user=user)

        # вывод данных в отображении
        context_data.update({'user': user, 'shop_stuff': shop_stuff, 'shop_stuff_favorites': shop_stuff_favorites, 'user_service': user_service})
        return render(request, 'users/shop.html', context_data)
    else:
        return auth


# страница не успешной авторизации пользователя
def login_fail(request):
    # обязательные данные
    context_data = get_context_data(request)

    # вывод данных в отображении
    return render(request, 'users/auth/fail.html', context_data)


# пополнение счета
def billing_payment(request):
    if request.POST:
        ik_am = request.POST.get('ik_am')

        user = User.objects.get(id=request.session['id'])
        billing_history = BillingHistory.objects.create(user=user, money=int(ik_am), score=int(ik_am))

        return redirect('https://sci.interkassa.com/?ik_co_id=' + settings.IK_CO_ID + '&ik_pm_no=' + str(billing_history.id) + '&ik_am=' + str(
            ik_am) + '&ik_cur=' + settings.IK_CUR + '&ik_desc=' + settings.IK_DESC)


# определяем статус счета после оплаты
@csrf_exempt
def billing_payment_status(request):
    try:
        billing_history = BillingHistory.objects.get(id=request.POST.get('ik_pm_no'))
        # обновляем статус платежа
        BillingHistory.objects.filter(id=request.POST.get('ik_pm_no')).update(payment_status=request.POST.get('ik_inv_st'))
        if request.POST.get('ik_inv_st') == 'success':
            # получаем биллиноговую информацию пользователя
            billing = Billing.objects.get(user_id=billing_history.user_id)
            money = int(billing.money) + int(billing_history.money)
            score = int(billing.score) + int(billing_history.score)
            # обновляем биллиноговую инфомрацию пользователя
            Billing.objects.filter(user=billing_history.user_id).update(money=money, score=score)
            return HttpResponse('ok', status=200)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('main:main'))


# страница после успешной оплаты счета
@csrf_exempt
def billing_payment_success(request):
    return HttpResponseRedirect(reverse('users:billing', args=(str(request.session['id']))))


# страница не успешной оплаты счета
@csrf_exempt
def billing_payment_fail(request):
    try:
        BillingHistory.objects.get(id=request.POST.get('ik_pm_no'))
        BillingHistory.objects.filter(id=request.POST.get('ik_pm_no')).update(payment_status=request.POST.get('ik_inv_st'))

        return HttpResponseRedirect(reverse('users:billing', args=(str(request.session['id']))))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('main:main'))


# страница успешной авторизации пользователя
def login_success(request):
    user = User.objects.get(username=request.user)
    request.session['id'] = user.id
    request.session['username'] = user.username
    request.session['email'] = user.email
    request.session['logged'] = True

    Billing.objects.get_or_create(user=user)
    Service.objects.get_or_create(user=user)

    return HttpResponseRedirect(reverse('main:main'))


# удаление авторизации
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main:main'))


# обновление данных пользователя
# стандартная модель пользователя
def user_update(request):
    if request.POST and request.is_ajax:
        user_id = request.session['id']
        username = request.POST.get('username')
        email = request.POST.get('email')

        try:
            User.objects.filter(id=user_id).update(username=username, email=email)
            data_res = {'status': 'success'}
        except ObjectDoesNotExist:
            data_res = {'status': 'fail'}
        return HttpResponse(json.dumps(data_res))


# обновление дополнительных данных пользователя
# дополнительная UserService модель пользователя
def user_service_update(request):
    if request.POST and request.is_ajax:
        user_id = request.session['id']
        exchange_link = request.POST.get('exchange_link')

        try:
            Service.objects.filter(user_id=user_id).update(exchange_link=exchange_link)
            messgage_response = {'status': 'success'}
        except ObjectDoesNotExist:
            messgage_response = {'status': 'fail'}
        return HttpResponse(json.dumps(messgage_response))
