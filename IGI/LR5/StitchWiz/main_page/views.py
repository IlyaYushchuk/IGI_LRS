from itertools import count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from matplotlib import pyplot as plt
# Create your views here.
from main_page.models import News, Question, Vacancy, Review, Coupon
from users.models import User, Master
from goods.models import Products, Categories
from main_page.forms import ReviewForm
from datetime import datetime, timezone
import pytz, tzlocal, calendar
import requests
import logging
from googletrans import Translator
from goods.models import Order
from django.db.models import Count


def canceled_orders(request):
    
    if request.user.is_master:
        orders = Order.objects.filter(is_canceled=True, master=request.user).order_by('date_order')
    else:
        orders = Order.objects.filter(is_canceled=True, user=request.user).order_by('date_order')

    context={
        'title':'Canceled orders',
        'order_name':'Отмененные заказы',
        'orders':orders
    }
    return render(request, 'orders.html', context)

def released_orders(request):

    if request.user.is_master:
        orders = Order.objects.filter(is_released=True, master=request.user).order_by('date_order')
    else:
        orders = Order.objects.filter(is_released=True, user=request.user).order_by('date_order')

    context={
        'title':'Realesed orders',
        'order_name':'Готовые заказы',
        'orders':orders
    }
    return render(request, 'orders.html', context)

def processing_orders(request):

    if request.user.is_master:
        orders = Order.objects.filter(is_processing=True, master=request.user).order_by('date_order')
    else:
        orders = Order.objects.filter(is_processing=True, user=request.user).order_by('date_order')

    context={
        'title':'Processing orders',
        'order_name':'Действующие заказы',
        'orders':orders
    }
    return render(request, 'orders.html', context)

def index(request):
    

    context = {
        'title':'Main',
        'content': 'Ремонт одежды и обуви StitchWiz',
        
    }
    return render(request, 'index.html',context)

def about(request):
    url_cat_fact = 'https://catfact.ninja/fact'
    cat_fact_en = requests.get(url_cat_fact).json()['fact']
    translator = Translator()
    cat_fact_ru = translator.translate(cat_fact_en, src='en', dest='ru').text

    
    url_rand_joke = 'https://official-joke-api.appspot.com/jokes/programming/random'
    rand_joke = requests.get(url_rand_joke).json()
    setup_ru = translator.translate(rand_joke[0]['setup'], src='en', dest='ru').text
    punchline_ru = translator.translate(rand_joke[0]['punchline'], src='en', dest='ru').text


    users_count = len(User.objects.all())
    
    orders = Order.objects.all()
    products = Products.objects.all()
    sales_incomes = [elem.get_price() for elem in orders]

    services_with_order_counts = Products.objects.annotate(order_count=Count('order')).order_by('-order_count')
    most_popular_product = services_with_order_counts.first()

    general_income = sum(sales_incomes)
    products_with_order_counts = Products.objects.annotate(order_count=Count('order'))
    
    vals = [elem.order_count for elem in products_with_order_counts]
    labels = [elem.name for elem in products]
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels, autopct='%1.1f%%')
    ax.axis("equal")
    fig.tight_layout()
    plt.savefig('main_page/static/images/graph.png')

   
    context = {
        'title':'About us',
        'content': 'Информация о нас',
        'text_on_page':'Данный сайт был написан для защиты 5 лабы по ИГИ',
        'cat_fact':cat_fact_ru,
        'setup':setup_ru,
        'punchline':punchline_ru,
        'users_count':users_count,
        'general_income':general_income,
        'most_popular_product':most_popular_product,

    }
    return render(request, 'about.html',context)

def news(request):
    news = News.objects.all()
    context = {
        'title':'News',
        'content': 'Информация о нас',
        'news':news
    }
    return render(request, 'news.html', context)

def new(request, new_id):
    new = News.objects.get(id=int(new_id))
    context = {
        'title':'News',
        'content': 'Информация о нас',
        'new':new
    }
    return render(request, 'new.html', context)
  
def questions(request):
    questions = Question.objects.all()

    context = {
        'title':'News',
        'questions': questions
    }
    return render(request, 'questions.html', context)

def staff(request):
    
    staff = User.objects.filter(is_staff=True)

    context = {
        'title':'Staff',
        'staff': staff
    }
    return render(request, 'staff.html', context)

def vacancies(request):

    vacancies = Vacancy.objects.all()

    context = {
        'title':'Vacancies',
        'vacancies': vacancies
    }
    return render(request, 'vacancies.html', context)

def reviews(request):

    reviews = Review.objects.all().order_by('-date')

    context = {
        'title':'Reviews',
        'reviews': reviews
    }
    return render(request, 'reviews.html', context)

def add_review(request):
    
    local_zone = tzlocal.get_localzone()
    date = datetime.now()
    utc_date = date.astimezone(pytz.utc)
   
    c = calendar.HTMLCalendar()
    s = c.formatmonth(date.year, date.month)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.date = date
            review.user = request.user
            review.save()
            return redirect('main_page:reviews')  # Замените на имя URL для списка отзывов или другой подходящий URL
    else:
        form = ReviewForm()

    context = {
        'title':'Add review',
        'form': form,
        'local_zone':local_zone,
        'date':date,
        'utc_date':utc_date,
        'calendar': s,
    }
    return render(request, 'add_review.html', context)

def coupons(request):

    now = datetime.now()

    valid_coupons = Coupon.objects.filter(date__gte=now)
    
    expired_coupons = Coupon.objects.filter(date__lt=now)

    context = {
        'title':'Coupons',
        'valid_coupons': valid_coupons,
        'expired_coupons': expired_coupons,
    }
    return render(request, 'coupons.html', context)