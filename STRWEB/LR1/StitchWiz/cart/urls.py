from django.urls import path, re_path
from cart import views

app_name = 'cart'

urlpatterns = [
    re_path(r'add/(?P<product_id>\d+)/', views.add_to_cart, name='add_to_cart'),
    re_path(r'delete/(?P<product_id>\d+)/', views.delete_from_cart, name='delete_from_cart'),
    re_path(r'edit/(?P<product_id>\d+)/(?P<type>\d+)/', views.edit_cart, name='edit_cart'),
    re_path(r'payment/', views.payment, name='cart_payment'),
    re_path(r'', views.cart, name='cart'),
]