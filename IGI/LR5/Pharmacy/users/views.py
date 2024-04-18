from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ReviewForm
from users.models import User, Questions, Review
from django.utils import timezone

from functions.menu import load_medicines

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
        'departments': load_medicines(),
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
        'departments': load_medicines(),
        'form': form
        }
    return render(request, 'users/registration.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def staff(request):
    users = User.objects.filter(is_staff=True)

    context = {
        'departments': load_medicines(),
        'staff': users
    }
    return render(request, 'users/staff.html', context)

def questions(request):
    questions = Questions.objects.all()

    context = {
        'departments': load_medicines(),
        'questions': questions[::-1]
    }
    return render(request, 'users/question-answer.html', context)

def profile(request):
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        grade = request.POST['grade']
        text = request.POST['review']
        if grade and text:
            review = Review()
            review.review = text
            review.grade = grade
            review.date = timezone.now()
            review.user = request.user
            review.save()
            return HttpResponseRedirect(reverse('users:reviews'))
    else:
        form = ReviewForm()

    context = {
        'departments': load_medicines(),
        'form': form
    }
    return render(request, 'users/profile.html', context)

def reviews(request):
    reviews = Review.objects.all()

    context = {
        'departments': load_medicines(),
        'reviews': reviews[::-1]
    }
    return render(request, 'users/review.html', context)