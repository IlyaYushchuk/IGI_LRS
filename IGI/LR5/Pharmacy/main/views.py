import requests
from django.shortcuts import render
from .models import New

from functions.menu import load_medicines

def index(request):
    appid = '53463e2c2ed3172e0488ab9e52e72b44'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = ['Brest', 'Vitebsk', 'Gomel', 'Grodno', 'Minsk', 'Mogilev']
    res = []
    for city in cities:
        temp = requests.get(url.format(city)).json()
        temp1 = {
            'city': city,
            'temp': temp["main"]["temp"],
            'icon': temp["weather"][0]["icon"],
            'values': [1, 2]
        }
        res.append(temp1)
    new = New.objects.first()
    print(res)
    context = {
        'departments': load_medicines(),
        'new': new,
        'weather': res
        }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'departments': load_medicines(),
        }
    return render(request, 'main/about.html', context)

def confidentialPolicy(request):
    url = 'https://official-joke-api.appspot.com/random_joke'
    joke = requests.get(url).json()

    context = {
        'departments': load_medicines(),
        'info': 'Здесь должна быть политика конфиденциальности, а пока что анекдот:',
        'setup': joke['setup'],
        'punchline': joke['punchline']
        }
    return render(request, 'main/confidentialPolicy.html', context)

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