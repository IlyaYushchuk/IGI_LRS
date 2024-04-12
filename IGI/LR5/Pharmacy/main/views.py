import requests
from django.shortcuts import render
from .models import New

from functions.menu import load_medicines

def index(request):
    context = {
        'departments': load_medicines(),
        'info' : 'qwerty'
        }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'departments': load_medicines(),
        'info' : '123456'
        }
    return render(request, 'main/about.html', context)

def news(request):
    news = New.objects.all()
    context = {
        'departments': load_medicines(),
        'news' : news
        }
    return render(request, 'main/news.html', context)

def new(request, new_id):
    new = New.objects.filter(id=new_id)[0]
    context = {
        'departments': load_medicines(),
        'new' : new
        }
    return render(request, 'main/new.html', context)