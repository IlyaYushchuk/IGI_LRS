from django.shortcuts import render, redirect

from goods.models import Products
from .models import  CartItem

def add_to_cart(request, product_id):

    items = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = CartItem.objects.filter(user=request.user, product=items)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            CartItem.objects.create(user=request.user, product=items, quantity=1)

    return redirect(request.META['HTTP_REFERER'])

def delete_from_cart(request, product_id):

    cart = CartItem.objects.get(user = request.user, id=product_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])

def edit_cart(request, product_id, type):

    cart = CartItem.objects.get(user = request.user, id=product_id)
    if type == '1':
        cart.quantity += 1
    elif type == '2':
        cart.quantity -= 1
        if cart.quantity == 0:
            delete_from_cart(request=request, product_id=product_id)
    cart.save()

    return redirect(request.META['HTTP_REFERER'])

def payment(request):

    items = CartItem.objects.filter(user=request.user)

    price = 0
    for item in items:
        price += item.quantity * item.product.sell_price()

    context = {
        'total': price
        }
    
    return render(request, 'cart/payment.html', context)

def cart(request):

    items = CartItem.objects.filter(user=request.user)

    price = 0
    for item in items:
        price += item.quantity * item.product.sell_price()

    context = {
        'items' : items,
        'total': price
        }
    return render(request, 'cart/cart.html', context)

