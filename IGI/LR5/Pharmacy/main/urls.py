from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('policy/', views.confidentialPolicy, name='policy'),
    path('news/', views.news, name='news'),
    path('news/<int:new_id>/', views.new, name='new'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('promotions/', views.promotions, name='promotions'),
    path('promotions/archive/', views.promotions, name='promotions_archive'),
    path('promotions/current/', views.promotions, name='promotions_current'),
]
