from multiprocessing import context
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from shop_app.models import Account, Drink, Ingredient, Order
from django.contrib.auth.models import User
import json
import random

from .forms import CreateUserForm

# Create your views here.
def home_general(request):
    template = loader.get_template('home_general.html')
    return HttpResponse(template.render())

def update_balance(request):
    accounts = Account.objects.all()
    current_account = None
    for account in accounts:
        if account.user == request.user:
            current_account = account
            current_account.balance += 100
            current_account.save()  
    return redirect('home')

def home(request):
    accounts = Account.objects.all()
    current_account = None
    current_drink = None
    goto_page = 'menu'
    for account in accounts:
        if account.user == request.user:
            current_account = account
    drinks = Drink.objects.all()
    ingredients = Ingredient.objects.all()
    orders = Order.objects.all()



    if request.method == "POST":
        if request.POST.get("update_username"):
            username = request.POST.get('username')
            request.user.username = username
            request.user.save()
            current_account.user = request.user
            current_account.save()
            goto_page = 'account'
        if request.POST.get("increase_balance"):
            current_account.balance += 100
            current_account.save()
            goto_page = 'account'
        for drink in drinks:
            if request.POST.get(drink.name):
                current_drink = drink
                goto_page = 'order_page'
        if request.POST.get("hire_employee"):
            employee_username = request.POST.get('account_type_change')
            current_account.hireEmployee(employee_username)
            accounts = Account.objects.all()
            goto_page = 'account'
        if request.POST.get("fire_employee"):
            employee_username = request.POST.get('account_type_change')
            current_account.fireEmployee(employee_username)
            accounts = Account.objects.all()
            goto_page = 'account'
        if request.POST.get("increase_hours"):
            current_account.addHours(4)
            goto_page = 'account'
        if request.POST.get("purchase_stock"):
            for ingredient in ingredients:
                ingredient.addStock(int(request.POST.get('inventory_' + ingredient.name)), current_account)
            goto_page = 'inventory'
        if request.POST.get("pay_employees"):
            print(current_account.payEmployees())
            accounts = Account.objects.all()
            goto_page = 'payroll'
        if request.POST.get("order_submit") or request.POST.get("customer_order_submit"):
            order_account = ''
            if request.POST.get("order_submit"):
                order_account = current_account
            elif request.POST.get("customer_order_submit"):
                order_username = request.POST.get("submission_username")
                for account in accounts:
                    if account.user.username == order_username:
                        order_account = account
                if order_account == '':
                    return 0


            ingredientCount = {}
            for ingredient in ingredients:
                ingredientCount[ingredient.name] = int(request.POST.get(ingredient.name))

            manager = ''
            for account in accounts:
                if account.user_type == 'Manager':
                    manager = account

            drink_name = request.POST.get("drink_name")
            drink_object = ''
            for drink in drinks:
                if drink.name == drink_name:
                    drink_object = drink

            while True:
                orderID = random.randint(-32000, 32000)
                for order in orders:
                    if order.orderNum == orderID:
                        continue
                break
            order_account.orderDrink(drink_object, ingredientCount, manager, orderID) 
            accounts = Account.objects.all()  
            orders = Order.objects.all()  
            ingredients = Ingredient.objects.all()     
        
        if request.POST.get('order_fulfill'):
            orderNum = int(request.POST.get('order_id'))
            for order in orders:
                if orderNum == order.orderNum:
                    selected_order = order
                    selected_order.fulfill(current_account)
                    break
            orders = Order.objects.all() 
            accounts = Account.objects.all()  
            goto_page = 'cash_register'     
            
        
    all_order_ingredients = {}
    for order in orders:
        all_order_ingredients[order.orderNum] = json.loads(order.ingredientsCount)

    return render(request, 'home.html', {'account': current_account, 'all_accounts': accounts, 'drinks': drinks, 'ingredients': ingredients, 'goto_page': goto_page, 'current_drink': current_drink, 'orders': orders, 'all_order_ingredients': all_order_ingredients})


def logon_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            accounts = Account.objects.all()
            account = None
            for temp in accounts: 
                if temp.user == user:        
                    account = temp
            if account.user_type == 'Manager':
                return redirect('home')
            elif account.user_type == 'Employee':
                return redirect('home')
            else:
                return redirect('home')

        else:
            messages.info(request, 'Login Credentials are Incorrect')
            return redirect('logon_page')
    context = {}
    return render(request, 'logon_page.html', context)

def logout_user(request):
    logout(request)
    return redirect('home_general')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            userlist = User.objects.all()
            for temp in userlist:
                if temp.username == username:
                    user = temp
            account = Account()
            account.user = user
            account.balance = 0.0
            account.save()
            return redirect('logon_page')


    context = {'form':form}
    return render(request, 'register.html', context)