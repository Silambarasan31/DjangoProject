from django.db import models

class Role(models.Model):

    role_name = models.CharField(max_length = 200)

    def __str__(self):
        
        return self.role_name

class EmployeeDetail(models.Model):

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 255)
    phone = models.CharField(max_length = 20)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)
    doj = models.DateField()
    salary = models.IntegerField(null = True)
    role = models.ForeignKey(Role, on_delete = models.CASCADE, null = True)
    def __str__(self):

        return f'{self.first_name} {self.last_name}'