from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^stats', views.stats, name='stats'),
    url(r'^video', views.video, name='video'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^send_email', views.send_email, name='send_email'),
    url(r'get_live_stats/', views.get_live_stats, name='get_live_stats'),
]
