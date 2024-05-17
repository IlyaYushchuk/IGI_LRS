from django.shortcuts import render

def login(request): 
    # if request.method == 'POST':
    #     form = UserLoginForm(data=request.POST)
    #     if form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = auth.authenticate(username=username, password=password)
    #         if user:
    #             auth.login(request, user)
    #             return HttpResponseRedirect(reverse('main:index'))
    # else:
    #     form = UserLoginForm()

    # context = {
    #     'departments': load_medicines(),
    #     'form': form
    # }

    return render(request, 'users/login.html')

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid() and request.POST.get('age_check', False):
#             form.save()
#             user = form.instance
#             auth.login(request, user)
#             return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserRegistrationForm()

#     context = {
#         'departments': load_medicines(),
#         'form': form
#         }
#     return render(request, 'users/registration.html', context)

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('main:index'))
