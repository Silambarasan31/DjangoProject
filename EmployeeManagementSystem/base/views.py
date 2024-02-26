from django.shortcuts import render, redirect
from .forms import RegisterUser, LoginUser, AddEmployeeForm, UpdateEmployeeForm   
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import EmployeeDetail, Role
from django.contrib import messages
from datetime import datetime

# Home page-index

def home(request):
    
    return render(request, 'base/index.html')

# Registering user

def register(request):


    if request.method == "POST":
        form = RegisterUser(request.POST)
        
        if form.is_valid():

                form.save()
                messages.success(request, "Registered successfully!")

                return redirect('login')
        
    
    form = RegisterUser()
    
    context = {'form' : form} 

    return render(request, 'base/register.html', context = context)


# Logging an user

def loginRequest(request):

    form = LoginUser()
    if request.method == "POST":

            form = LoginUser(request.POST)

        
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username= username, password= password)

            
            if user:
                
                
                auth.login(request, user)
                
                return redirect('dashboard')
            
                

            else:
                messages.error(request, "Incorrect Username/Password")
                
                return redirect('login')
    
        

    context = {'form': form}

    return render(request, 'base/login.html', context = context)
        
# - user logout

def userLogout(request):

    auth.logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('login')

# - Dashboard
@login_required(login_url = 'login')
def dashboard(request):

    all_records = EmployeeDetail.objects.all()
    all_role = Role.objects.all()

    count = list(range(1,len(all_records)+1))
    zipped_list = zip(all_records,count)
    context = {
        'all_emp' : zipped_list,
        'all_role' : all_role
    }
    return render(request, 'base/dashboard.html', context)

#-Create a record

@login_required(login_url = 'login')
def add_employee(request):
    
    if request.method == 'POST':

        form = AddEmployeeForm(request.POST)

        if form.is_valid():
            form.save()
           

            messages.success(request, "Employee added!")

            return redirect('dashboard')
        context = {'form': form}

        return render(request, "base/add_employee.html", context)
    else:
        role = Role.objects.all()
        context = {'role':role}
        return render(request,"base/add_employee.html", context)
    
    
def mdy_to_ymd(d):
     return datetime.strptime(d, '%b. %d, %Y').strftime('%Y-%m-%d')
#-update a record

@login_required(login_url = 'login')
def update_employee(request, emp_id):

    record = EmployeeDetail.objects.get(id = emp_id) 
    

    if request.method == 'POST':
        
        form = UpdateEmployeeForm(request.POST, instance=record)

        form.save()

        return redirect('dashboard')
    
    else:
        role = Role.objects.all()       
        context = {
            'role':role,
            'record':record
                   }
          
        return render(request,"base/update_employee.html", context)


#-view a single record

@login_required(login_url = 'login')
def view_employee(request, emp_id):

    all_detail = EmployeeDetail.objects.get(id = emp_id)

    context = {
        'detail' : all_detail
    }

    return render(request, 'base/view_employee.html', context)

#-delete a single record

@login_required(login_url = 'login')
def delete_employee(request, emp_id):

    emp_detail = EmployeeDetail.objects.get(id = emp_id)

    

    emp_detail.delete()

    return redirect('dashboard')