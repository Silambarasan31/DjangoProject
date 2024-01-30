from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms.widgets import TextInput, PasswordInput

# - Register user

class RegisterUser(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

# - Login registered user

class LoginUser(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())