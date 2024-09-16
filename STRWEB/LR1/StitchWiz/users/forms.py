from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User

class UserLoginForm(AuthenticationForm):
    
    class Meta:
        model = User
    
    username = forms.CharField()
    password = forms.CharField()

        
class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields=(
        'first_name',
        'last_name',
        'username',
        'phone',
        'email',
        'password1', 
        'password2')


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields=(
        'image',
        'first_name',
        'last_name',
        'username',
        'phone',
        'email',
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
    

