import requests
from django.shortcuts import render
from .models import New
from Medicines.models import Departments

def load_medicines():
    return Departments.objects.all()

def index(request):
    info = {
        'info': 'qwerty',
        'departments': load_medicines()
        }
    context = {'info' : info}
    return render(request, 'main/base.html', context)

def about(request):
    info = {
        'info': '123456',
        'departments': load_medicines()
        }
    context = {'info' : info}
    return render(request, 'main/about.html', context)

def news(request):
    #obj = New.objects.create(title='Head', some_info='some info about this new', text='this is text about this new that you choose.')

    news = New.objects.filter(title='Head')
    news_list = []
    for new in news:
        temp = {
            'title': new.title,
            'some_info': new.some_info,
            'text': new.text
        }
        news_list.append(temp)
    info = {
        'info': news_list,
        'departments': load_medicines()
        }
    context = {'info' : info}
    return render(request, 'main/news.html', context)