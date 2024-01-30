from django.shortcuts import render, redirect
from .forms import RegisterUser, LoginUser   
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Home page-index

def home(request):
    
    return render(request, 'base/index.html')

# Registering user

def register(request):


    if request.method == "POST":
        form = RegisterUser(request.POST)

        if form.is_valid:

            form.save()

            return redirect('login')
    else:
        form = RegisterUser()
    
    context = {'form' : form} 

    return render(request, 'base/register.html', context = context)


# Logging an user

def loginRequest(request):


    if request.method == "POST":

        form = LoginUser(request.POST)

        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username, password= password)

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')

    else:
        form = LoginUser()

    context = {'form': form}

    return render(request, 'base/login.html', context = context)
        
# - user logout

def userLogout(request):

    auth.logout(request)

    return redirect('login')

# - Dashboard
@login_required(login_url = 'login')
def dashboard(request):

    return render(request, 'base/dashboard.html')