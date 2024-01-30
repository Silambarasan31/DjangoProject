from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name= ''),
    path('register', views.register, name = "register"),
    path('login', views.loginRequest, name = "login"),
    path('logout', views.userLogout, name = "logout"),
    path('dashboard', views.dashboard, name = "dashboard"),

]