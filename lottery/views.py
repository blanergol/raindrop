from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json, random

from main.views import get_context_data
from django.contrib.auth.models import User
from .models import Briefcases, DotaboxModes, Stuff
from users.models import HistoryGames, Inventory, Billing


# страница режима RDCASE
def briefcases(request):
    # обязательные данные
    context_data = get_context_data(request)

    briefcases = Briefcases.objects.all().order_by('id')

    # вывод данных в отображении
    context_data.update({'briefcases': briefcases})
    return render(request, 'lottery/briefcases.html', context_data)


# страница подробного просмотра кейса для режима RDCASE
def briefcases_full(request, pk):
    # обязательные данные
    context_data = get_context_data(request)

    case = Briefcases.objects.get(id=pk)
    case_stuff = case.stuff.filter(show_status=True).order_by('?')
    case_stuff_count = case_stuff.count()

    case_stuff_tmp = []
    for i in case_stuff:
        case_stuff_tmp.append(i)
    for i in case_stuff:
        case_stuff_tmp.append(i)
    for i in case_stuff:
        case_stuff_tmp.append(i)
    for i in case_stuff:
        case_stuff_tmp.append(i)
    for i in case_stuff:
        case_stuff_tmp.append(i)
    for i in case_stuff:
        case_stuff_tmp.append(i)

    stats_live = HistoryGames.objects.all().order_by('date')[:4]

    # вывод данных в отображении
    context_data.update({'case': case, 'case_stuff': case_stuff, 'stats_live': stats_live, 'case_stuff_count': case_stuff_count, 'case_stuff_tmp': case_stuff_tmp})
    return render(request, 'lottery/briefcases_full.html', context_data)


# страница режима DOTABOX
def dotabox(request, pk):
    # обязательные данные
    context_data = get_context_data(request)

    dotabox_modes = DotaboxModes.objects.filter(enable=True).order_by('id')
    dotabox_mode = DotaboxModes.objects.get(id=pk)
    dotabox_stuff = dotabox_mode.stuff.filter(show_status=True)
    dotabox_stuff_count = dotabox_stuff.count()

    # вывод данных в отображении
    context_data.update({'dotabox_modes': dotabox_modes, 'dotabox_mode': dotabox_mode, 'dotabox_stuff': dotabox_stuff, 'dotabox_stuff_count': dotabox_stuff_count})
    return render(request, 'lottery/dotabox.html', context_data)


# страница режима MAGICK BALL
def magick_ball(request):
    # обязательные данные
    context_data = get_context_data(request)

    # вывод данных в отображении
    return render(request, 'lottery/magick_ball.html', context_data)


# страница режима TECHIES
def techies(request):
    # обязательные данные
    context_data = get_context_data(request)

    # вывод данных в отображении
    return render(request, 'lottery/techies.html', context_data)


# розыгрыш вещи для режима DOTABOX
def dotabox_action(request):
    if request.POST and request.is_ajax:
        id_dotabox = request.POST.get('id_dotabox')

        # проверяем авторизован ли пользователь
        if 'id' in request.session:
            # получили пользователя
            user = User.objects.get(id=request.session['id'])
            # загрузили данные по режиму игры
            dotabox_mode = DotaboxModes.objects.get(id=id_dotabox)
            # загрузили вещи для режима
            dotabox_stuff = dotabox_mode.stuff.filter(show_status=True)
            # загрузили платежную информацию по пользователю
            billing = Billing.objects.get(user=user)
            if dotabox_mode.score < billing.score:
                # получаем 4 вещи для режима игры
                stuff_all = dotabox_stuff.order_by('?')[:4]
                # получаем случайную вещь
                # TODO:алгоритм получения вещи для Dota Box
                stuff = stuff_all.first()
                # перемешиываем 4 кейса
                # что бы убрать видимость сортировки для пользователя
                stuff_all = sorted(stuff_all, key=lambda x: random.random())
                # убираем вещь из розыгрыша
                Stuff.objects.filter(id=stuff.id).update(show_status=False)
                # добвляем игру в историю игр
                HistoryGames.objects.create(user=user, stuff=stuff, type='dotabox')
                # добалявем вещь на аккаунт пользователя
                stuff = Inventory.objects.create(user=user, stuff=stuff, type='games')
                # обновляем платежную информацию пользователя
                billing.score -= dotabox_mode.score
                billing.save()

                message_response = {'status': 'success', 'type_game': 'pay',
                                    'stuff': {'img': stuff.stuff.img.url, 'title': stuff.stuff.title, 'score': stuff.stuff.score},
                                    'case_all': {'case1': stuff_all[0].score, 'case2': stuff_all[1].score, 'case3': stuff_all[2].score, 'case4': stuff_all[3].score}}
            else:
                message_response = {'status': 'fail'}
        # если нет, проводим для него тестовую игру
        else:
            # загрузили данные по режиму игры
            dotabox_mode = DotaboxModes.objects.get(id=id_dotabox)
            # загрузили вещи для режима
            dotabox_stuff = dotabox_mode.stuff.filter(show_status=True)
            # получаем 4 вещи для режима игры
            stuff_all = dotabox_stuff.order_by('-score')[:4]
            # получаем случайную вещь
            stuff = stuff_all.first()
            # перемешиываем 4 кейса
            # что бы убрать видимость сортировки для пользователя
            stuff_all = sorted(stuff_all, key=lambda x: random.random())
            message_response = {'status': 'success', 'type_game': 'free',
                                'stuff': {'img': stuff.img.url, 'title': stuff.title, 'score': stuff.score},
                                'case_all': {'case1': stuff_all[0].score, 'case2': stuff_all[1].score, 'case3': stuff_all[2].score, 'case4': stuff_all[3].score}}
        return HttpResponse(json.dumps(message_response))


# розыгрыш вещи для режима RDCASE
def rdcase_action(request):
    if request.POST and request.is_ajax:
        id_case = request.POST.get('id_case')

        # получили пользователя
        user = User.objects.get(id=request.session['id'])
        # загрузили данные по кейсу
        briefcases = Briefcases.objects.get(id=id_case)
        # загрузили вещи для кейса
        case_stuff = briefcases.stuff.filter(show_status=True)
        # загрузили платежную информацию по пользователю
        billing = Billing.objects.get(user=user)

        # если хватает средств на аккаунте
        if briefcases.score < billing.score:
            # получаем случайную вещь
            # TODO:алгоритм получения вещи в RD Case
            stuff = case_stuff.order_by('?').first()
            # убираем вещь из розыгрыша
            Stuff.objects.filter(id=stuff.id).update(show_status=False)
            # добвляем игру в историю игр
            HistoryGames.objects.create(user=user, stuff=stuff, type='rdcase')
            # добалявем вещь на аккаунт пользователя
            stuff = Inventory.objects.create(user=user, stuff=stuff, type='games')
            # обновляем платежную информацию пользователя
            billing.score -= briefcases.score
            billing.save()

            message_response = {'status': 'success',
                                'content': {'img': stuff.stuff.img.url, 'title': stuff.stuff.title, 'score': stuff.stuff.score}}
        else:
            message_response = {'status': 'fail'}
        return HttpResponse(json.dumps(message_response))


# продажа выигранной вещи
def sell_stuff(request):
    if request.POST and request.is_ajax():
        stuff_id = request.POST.get('stuff_id')

        user = User.objects.get(id=request.session['id'])
        try:
            # поверяем на существование вещи
            stuff = Stuff.objects.get(id=stuff_id)
            try:
                # проверяем принадлжеит ли вещь пользователю
                stuff = Inventory.objects.get(stuff=stuff, user=user)
                # получаем биллинговую инфомрацию по пользователю
                billing = Billing.objects.get(user=user)
                # обновляем биллинговую информацию пользователя
                # TODO:проценты за продажу вещи
                Billing.objects.filter(user=user).update(user=user, score=stuff.stuff.score + billing.score)
                # удаляем вещь из аккаунта пользователя
                Inventory.objects.filter(user=user, stuff_id=stuff_id).delete()
                # размещаем вещь в магазине
                Stuff.objects.filter(id=stuff_id).update(show_shop_status=True, show_status=True)
                message_response = {'status': 'success'}
            except ObjectDoesNotExist:
                message_response = {'status': 'fail'}
        except ObjectDoesNotExist:
            message_response = {'status': 'fail'}
        return HttpResponse(json.dumps(message_response))
