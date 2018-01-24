from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'users/(?P<pk>[0-9]+)/$', views.profile, name='profile'),
    url(r'users/(?P<pk>[0-9]+)/history_games', views.history_games, name='history_games'),
    url(r'users/(?P<pk>[0-9]+)/shop', views.shop, name='shop'),

    # inventory start
    url(r'users/(?P<pk>[0-9]+)/inventory', views.inventory, name='inventory'),
    # inventory end

    url(r'users/login_success', views.login_success, name='login_success'),
    url(r'users/login_fail', views.login_fail, name='login_fail'),
    url(r'users/logout', views.logout, name='logout'),
    url(r'users/user_update', views.user_update, name='user_update'),
    url(r'users/user_service_update', views.user_service_update, name='user_service_update'),

    # billing start
    url(r'users/(?P<pk>[0-9]+)/billing', views.billing, name='billing'),
    url(r'billing/success', views.billing_payment_success, name='billing_payment_success'),
    url(r'billing/fail', views.billing_payment_fail, name='billing_payment_fail'),
    url(r'billing/status', views.billing_payment_status, name='billing_payment_status'),
    url(r'billing/payment', views.billing_payment, name='billing_payment'),
    # billing end
]
