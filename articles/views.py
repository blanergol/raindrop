from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from main.views import get_context_data, get_top_users
from .models import Articles
from settings.models import Settings


def main(request):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    # получение статистики по популярных пользователям
    top_users = get_top_users()

    settings = Settings.objects.first()
    articles = Articles.objects.all()
    articles_best = articles.order_by('-views')[:5]
    articles = articles.order_by('-created_date')
    paginator = Paginator(articles, settings.count_posts)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    # вывод данных в отображении
    context_data.update({'articles': articles, 'articles_best': articles_best, 'top_users': top_users})
    return render(request, 'articles/main.html', context_data)


def full(request, pk):
    # загрузка обязательных данных
    context_data = get_context_data(request)

    # получение статистики по популярных пользователям
    top_users = get_top_users()

    article = get_object_or_404(Articles, pk=pk)
    article.views += 1
    article.save()

    # вывод данных в отображении
    context_data.update({'article': article, 'top_users': top_users})
    return render(request, 'articles/full.html', context_data)
