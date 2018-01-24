"""fmball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url('', include('social_django.urls', namespace='social')),
    url(r'', include('main.urls', namespace='main')),
    url(r'', include('articles.urls', namespace='articles')),
    url(r'', include('pages.urls', namespace='pages')),
    url(r'', include('lottery.urls', namespace='lottery')),
    url(r'', include('users.urls', namespace='users')),
    url(r'', include('shop.urls', namespace='shop'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += [
        url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
