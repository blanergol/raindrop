from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'pages/(?P<pk>[0-9]+)/$', views.pages, name='pages'),
]