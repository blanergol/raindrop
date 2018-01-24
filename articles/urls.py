from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'articles/(?P<pk>[0-9]+)/$', views.full, name='full'),
    url(r'articles', views.main, name='main'),
]
