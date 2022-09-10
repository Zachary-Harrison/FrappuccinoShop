from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Here is the beginning of our Dan's Frappuccino Paradise shop app.")