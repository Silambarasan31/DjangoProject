from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name= ''),
    path('register', views.register, name = "register"),
    path('login', views.loginRequest, name = "login"),
    path('logout', views.userLogout, name = "logout"),

    path('dashboard', views.dashboard, name = "dashboard"),
    path('add-employee', views.add_employee, name = "add-employee"),
    path('update-employee/<int:emp_id>', views.update_employee, name = "update-employee"),
    path('view-employee/<int:emp_id>', views.view_employee, name = "view-employee"),
    path('delete-employee/<int:emp_id>', views.delete_employee, name = "delete-employee"),

]