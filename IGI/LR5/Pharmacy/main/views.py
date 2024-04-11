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
    news = New.objects.filter(title='Head')
    news_list = []
    for new in news:
        temp = {
            'title': new.title,
            'some_info': new.some_info,
            'text': new.text
        }
        news_list.append(temp)
    context = {
        'departments': load_medicines(),
        'info' : news_list
        }
    return render(request, 'main/news.html', context)