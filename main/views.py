from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
import json

from django.contrib.auth.models import User
from .models import Video, About, Contact
from settings.models import Settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from articles.models import Articles
from pages.models import Pages
from users.models import HistoryGames, Billing
from lottery.models import Stuff


# получение повторяющихся данных в отображении
def get_context_data(request):
    # обязательные данные
    settings = Settings.objects.first()
    articles_footer = Articles.objects.all().order_by('-created_date')[:3]
    pages_header = Pages.objects.all().filter(show_status=True)
    history_games_header = HistoryGames.objects.all()[:5]

    # проверка на авторизацию пользователя и вывод биллинговой информации
    try:
        if 'id' in request.session:
            user_id = request.session['id']
        else:
            user_id = -1
        billing = Billing.objects.get(user_id=user_id)
    except ObjectDoesNotExist:
        billing = None

    context_data = {'settings': settings, 'articles_footer': articles_footer, 'pages_header': pages_header, 'history_games_header': history_games_header,
                    'billing': billing}
    return context_data


# получение статистики по популярных пользователям
def get_top_users():
    all_users = User.objects.filter(is_superuser=0)
    top_users = []
    score = 0
    count_stuff = 0
    for user in all_users:
        history_games_user = HistoryGames.objects.filter(user_id=user.id)
        for item in history_games_user:
            score = score + item.stuff.score
            count_stuff = count_stuff + 1

        user_tmp = {'user': user, 'count_stuff': count_stuff, 'score': score}
        top_users.append(user_tmp)
    return top_users


def main(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    articles = Articles.objects.all()
    articles_best = articles.order_by('-views')[:5]
    articles = articles.order_by('-created_date')[:4]
    video = Video.objects.all().order_by('-created_date')[:4]

    # получение статистики по популярных пользователям
    top_users = get_top_users()
    stats_live = HistoryGames.objects.all().order_by('date')[:4]

    # количество совершенных игр
    rdcase_hs = HistoryGames.objects.filter(type='rdcase').count()
    dotabox_hs = HistoryGames.objects.filter(type='dotabox').count()
    magick_hs = HistoryGames.objects.filter(type='magick_ball').count()
    techies_hs = HistoryGames.objects.filter(type='techies').count()
    count_history_games = {'rdcase': rdcase_hs, 'dotabox': dotabox_hs, 'magick_ball': magick_hs, 'techies': techies_hs}

    # количество текущего и проданного товара в магазиге
    count_stuff_shop = Stuff.objects.filter(show_shop_status=True).count()
    count_stuff_sales_shop = Stuff.objects.filter(show_shop_status=False).count()
    count_stuff = {'shop': count_stuff_shop, 'sales': count_stuff_sales_shop}

    # вывод данных в отображении
    context_data.update({'articles_best': articles_best, 'articles': articles, 'video': video, 'top_users': top_users, 'stats_live': stats_live,
                         'count_history_games': count_history_games, 'count_stuff': count_stuff})
    return render(request, 'main/main.html', context_data)


def stats(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    users_count = User.objects.filter(is_superuser=0).count()
    history_games = HistoryGames.objects.all()
    history_games_count = history_games.count()
    money_games = 0
    for game in history_games:
        money_games = money_games + game.stuff.score

    top_users = get_top_users()
    stats = {'top_users': top_users, 'users_count': users_count, 'history_games_count': history_games_count, 'money_games': money_games}

    # вывод данных в отображении
    context_data.update({'stats': stats})
    return render(request, 'main/stats.html', context_data)


def video(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    settings = Settings.objects.first()
    video = Video.objects.all().order_by('-created_date')
    paginator = Paginator(video, settings.count_video)
    page = request.GET.get('page')
    try:
        video = paginator.page(page)
    except PageNotAnInteger:
        video = paginator.page(1)
    except EmptyPage:
        video = paginator.page(paginator.num_pages)

    # вывод данных в отображении
    context_data.update({'video': video})
    return render(request, 'main/video.html', context_data)


def about(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    about = About.objects.first()

    # вывод данных в отображении
    context_data.update({'about': about})
    return render(request, 'main/about.html', context_data)


def contact(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    contact = Contact.objects.first()

    # вывод данных в отображении
    context_data.update({'contact': contact})
    return render(request, 'main/contact.html', context_data)


def send_email(request):
    settings = Settings.objects.first()

    if request.POST and request.is_ajax:
        name = request.POST.get('contact-form-name')
        email = request.POST.get('contact-form-email')
        subject = request.POST.get('contact-form-subject')
        message_tmp = request.POST.get('contact-form-message')

        message = 'Имя: ' + str(name) + '\n' + 'Email: ' + str(email) + '\n' + 'Сообщение: ' + str(message_tmp)

        if send_mail(subject, message, email, [settings.email]):
            message_response = {'status': 'success'}
        else:
            message_response = {'status': 'fail'}
        return HttpResponse(json.dumps(message_response))


@csrf_exempt
def get_live_stats(request):
    history_games = HistoryGames.objects.filter(date__lt=timezone.now()).order_by('date')
    message_response = JsonResponse({'status': 'success', 'data': serializers.serialize('json', history_games)})
    return HttpResponse(message_response)
