from multiprocessing import context
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

# Create your views here.
def home_general(request):
    template = loader.get_template('home_general.html')
    return HttpResponse(template.render())


def home_customer(request):
    template = loader.get_template('home_customer.html')
    return HttpResponse(template.render())


def home_employee(request):
    template = loader.get_template('home_employee.html')
    return HttpResponse(template.render())
    
def home_manager(request):
    template = loader.get_template('home_manager.html')
    return HttpResponse(template.render())


def account_customer(request):
    template = loader.get_template('account_customer.html')
    return HttpResponse(template.render())

def account_employee(request):
    template = loader.get_template('account_employee.html')
    return HttpResponse(template.render())

def account_manager(request):
    template = loader.get_template('account_manager.html')
    return HttpResponse(template.render())

def menu_customer(request):
    template = loader.get_template('menu_customer.html')
    return HttpResponse(template.render())

def menu_employee(request):
    template = loader.get_template('menu_employee.html')
    return HttpResponse(template.render())

def menu_manager(request):
    template = loader.get_template('menu_manager.html')
    return HttpResponse(template.render())

def cashier_employee(request):
    template = loader.get_template('cashier_employee.html')
    return HttpResponse(template.render())

def cashier_manager(request):
    template = loader.get_template('cashier_manager.html')
    return HttpResponse(template.render())

def stock_manager(request):
    template = loader.get_template('stock_manager.html')
    return HttpResponse(template.render())

def pay_page_manager(request):
    template = loader.get_template('pay_page_manager.html')
    return HttpResponse(template.render())


def logon_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_general')
        else:
            messages.info(request, 'Login Credentials are Incorrect')
            return redirect('logon_page')
    context = {}
    return render(request, 'logon_page.html', context)

def logoutUser(request):
    logout(request)
    return redirect('logon_page')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('logon_page')


    context = {'form':form}
    return render(request, 'register.html', context)