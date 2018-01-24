from django.conf.urls import url
from . import views

urlpatterns = [
    # dotabox start
    url(r'dotabox/(?P<pk>[0-9]+)/$', views.dotabox, name='dotabox'),
    url(r'dotabox/dotabox_action/', views.dotabox_action, name='dotabox_action'),
    # dotabox end

    # briefcases start
    url(r'briefcases/rdcase_action/', views.rdcase_action, name='rdcase_action'),
    url(r'briefcases/(?P<pk>[0-9]+)/$', views.briefcases_full, name='briefcases_full'),
    url(r'briefcases/', views.briefcases, name='briefcases'),
    # briefcases end

    # magick_ball start
    url(r'magick_ball/', views.magick_ball, name='magick_ball'),
    # magick_ball end

    # techies start
    url(r'techies/', views.techies, name='techies'),
    # techies end

    url(r'lottery/sell_stuff', views.sell_stuff, name='sell_stuff'),
]
