from django.urls import path, include

from main_page import views

app_name = 'main_page'

urlpatterns = [    
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
]
