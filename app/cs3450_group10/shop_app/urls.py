from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_general, name ='home_general'),
    path('home_general', views.home_general, name ='home_general'),
    path('logon_page', views.logon_page, name = 'logon_page'),

    path('logout_user', views.logout_user, name='logout_user'),
    path('register', views.registerPage, name="register"),

    path('home', views.home, name='home'),

    path('update_balance', views.update_balance, name="update_balance"),

]