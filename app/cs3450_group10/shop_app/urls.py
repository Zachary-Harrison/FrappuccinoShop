from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_general, name ='home_general'),
    path('home_general', views.home_general, name ='home_general'),
    path('home_customer', views.home_customer, name ='home_customer'),
    path('home_employee', views.home_employee, name ='home_employee'),
    path('home_manager', views.home_manager, name ='home_manager'),
    path('logon_page', views.logon_page, name = 'logon_page'),
    path('account_customer', views.account_customer, name='account_customer'),
    path('account_employee', views.account_employee, name='account_employee'),
    path('account_manager', views.account_manager, name='account_manager'),
    path('menu_customer', views.menu_customer, name="menu_customer"),
    path('menu_employee', views.menu_employee, name="menu_employee"),
    path('menu_manager', views.menu_manager, name="menu_manager"),
    path('cashier_employee', views.cashier_employee, name="cashier_employee"),
    path('cashier_manager', views.cashier_manager, name="cashier_manager"),
    path('stock_manager', views.stock_manager, name="stock_manager"),
    path('pay_page_manager', views.pay_page_manager, name="pay_page_manager"),

    path('logout_user', views.logout_user, name='logout_user'),
    path('register', views.registerPage, name="register"),

    path('update_balance', views.update_balance, name="update_balance"),

]