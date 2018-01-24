from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'shop/payment', views.payment, name='payment'),
    url(r'shop/favorites_remove', views.favorites_remove, name='favorites_remove'),
    url(r'shop/favorites', views.favorites, name='favorites'),
    url(r'shop/search', views.search, name='search'),
    url(r'shop/remove_sell_stuff', views.remove_sell_stuff, name='remove_sell_stuff'),
    url(r'shop/filter_price', views.filter_price, name='filter_price'),
    url(r'shop/sell_stuff', views.sell_stuff, name='sell_stuff'),
    url(r'shop/', views.main, name='main'),
]
