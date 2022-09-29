from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_general, name ='home_general'),
    path('home_general', views.home_general, name ='home_general'),
    path('logon', views.logon, name = 'logon'),
    path('home_customer', views.home_customer, name ='home_customer'),
    path('account', views.account, name='account'),
    path('menu', views.menu, name="menu")
]