import requests
from django.shortcuts import render
from .models import New, Vacancy, Promotion
from users.models import User
from Medicines.models import Sales

from functions.menu import load_medicines
from datetime import datetime
import statistics

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

def vacancies(request):
    vacancies = Vacancy.objects.all()
    context = {
        'departments': load_medicines(),
        'vacancies': vacancies
        }
    return render(request, 'main/vacancy.html', context)

def promotions(request):
    date_now = datetime.now()
    promotions = []
    if '/promotions/archive/' == request.path:
        promotions = Promotion.objects.filter(date__lte=date_now)
    elif '/promotions/current/' == request.path:
        promotions = Promotion.objects.filter(date__gte=date_now)
    else:
        promotions = Promotion.objects.all()

    promotions = [*promotions]
    promotions.sort(key=lambda elem: elem.date, reverse=True)
    
    context = {
        'departments': load_medicines(),
        'promotions': promotions
        }
    return render(request, 'main/promotion.html', context)

def statistic(request):
    users_count = len(User.objects.all())
    
    sales = Sales.objects.all()
    sales_incomes = [elem.medicine.price * elem.quantity for elem in sales]

    general_income = sum(sales_incomes)
    popular_med = max([elem for elem in sales], key=lambda elem: elem.quantity).medicine.name
    most_income_med = max([elem for elem in sales], key=lambda elem: elem.medicine.price * elem.quantity).medicine.name

    context = {
        'departments': load_medicines(),
        'users_count': users_count,
        'income': general_income,
        'popular_med': popular_med,
        'most_income_med': most_income_med,
        'sales_average': statistics.mean(sales_incomes),
        'sales_mode': statistics.mode(sales_incomes),
        'sales_median': statistics.median(sales_incomes),
        'sales_variance': statistics.variance(sales_incomes),
        'sales_stdev': statistics.stdev(sales_incomes)
        }
    return render(request, 'main/statistic.html', context)