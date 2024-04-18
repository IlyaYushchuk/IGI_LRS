from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('staff/', views.staff, name='staff'),
    path('questions/', views.questions, name='questions'),
    path('profile/', views.profile, name='profile'),
    path('reviews/', views.reviews, name='reviews'),
]
