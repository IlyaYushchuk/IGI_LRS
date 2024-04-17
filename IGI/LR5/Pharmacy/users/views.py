from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid() and request.POST.get('age_check', False):
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
            'form': form
        }
    return render(request, 'users/registration.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def staff(request):
    users = User.objects.filter(is_staff=True)

    context = {
        'staff': users
    }
    return render(request, 'users/staff.html', context)
