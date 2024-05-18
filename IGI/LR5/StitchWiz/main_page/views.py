from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from goods.models import Categories

def index(request):

  

    context = {
        'title':'Main',
        'content': 'Ремонт одежды и обуви StitchWiz',
    }
    return render(request, 'index.html',context)


def about(request):
    context = {
        'title':'About us',
        'content': 'Информация о нас',
        'text_on_page':'Данный сайт был написан для защиты 5 лабы по ИГИ'
    }
    return render(request, 'about.html',context)
