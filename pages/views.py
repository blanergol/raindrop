from django.shortcuts import render, get_object_or_404

from main.views import get_context_data
from .models import Pages


def pages(request, pk):
    # обязательные данные
    context_data = get_context_data(request)

    page = get_object_or_404(Pages, pk=pk)

    # вывод данных в отображении
    context_data.update({'page': page})
    return render(request, 'pages/main.html', context_data)
