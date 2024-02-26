from django.contrib import admin

from .models import EmployeeDetail, Role

admin.site.register(EmployeeDetail)
admin.site.register(Role)