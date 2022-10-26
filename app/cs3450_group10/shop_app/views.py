from multiprocessing import context
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from shop_app.models import Account, Drink, Ingredient
from django.contrib.auth.models import User

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
    goto_page = 'menu'
    for account in accounts:
        if account.user == request.user:
            current_account = account
    drinks = Drink.objects.all()
    ingredients = Ingredient.objects.all()

    if request.method == "POST":
        if request.POST.get("update_username"):
            username = request.POST.get('username')
            request.user.username = username
            request.user.save()
            current_account.user = request.user
            current_account.save()
            goto_page = 'account'
        if request.POST.get("increase_balance"):
            print("increasing balance")
            current_account.balance += 100
            current_account.save()
            goto_page = 'account'


    return render(request, 'home.html', {'account': current_account, 'drinks': drinks, 'ingredients': ingredients, 'goto_page': goto_page})


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