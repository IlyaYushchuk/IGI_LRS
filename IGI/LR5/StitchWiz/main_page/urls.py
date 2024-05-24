from django.urls import path, re_path, include

from main_page import views

app_name = 'main_page'

urlpatterns = [    
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('news/',views.news, name='news'),
    re_path(r'news/(?P<new_id>\d+)/', views.new, name='new'),
    path('questions/', views.questions, name='questions'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('staff/', views.staff, name='staff'),
    path('reviews/', views.reviews, name='reviews'),
    path('add_review/', views.add_review, name='add_review'),
    path('coupons/', views.coupons, name='coupons'),
    path('processing_orders/', views.processing_orders, name = 'processing_orders'),
    path('canceled_orders/', views.canceled_orders, name = 'canceled_orders'),
    path('released_orders/', views.released_orders, name = 'released_orders'),
  
]

