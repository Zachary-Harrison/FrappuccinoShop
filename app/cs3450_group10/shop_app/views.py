from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home_general(request):
    template = loader.get_template('home_general.html')
    return HttpResponse(template.render())
    
def logon(request):
    template = loader.get_template('logon_page.html')
    return HttpResponse(template.render())

def account(request):
    template = loader.get_template('account.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())

def home_customer(request):
    template = loader.get_template('home_customer.html')
    return HttpResponse(template.render())