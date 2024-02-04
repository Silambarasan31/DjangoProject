from django.db import models

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

    def __str__(self):

        return f'{self.first_name} {self.last_name}'

#     projects = models.ManyToManyField('Project')

# class Project(models.Model):

#     project_name = models.CharField(max_length = 255)
#     # related = models.ForeignKey('EmployeeDetail', on_delete = models.CASCADE)
#     project_startdate = models.DateField(null = True)
#     project_enddate = models.DateField(null = True)

# class Role(models.Model);

