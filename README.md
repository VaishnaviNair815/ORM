# Ex02 Django ORM Web Application
## Date: 13.04.2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py 
from django.db import models
from django.contrib import admin
class Employee(models.Model):
    USER_ID = models.IntegerField(primary_key=True)
    USER_NAME = models.CharField(max_length=100)
    PHONE_NUMBER = models.IntegerField()
    EMAIL = models.EmailField()
    MOVIE_NAME = models.CharField(max_length=100)
    SEATS = models.IntegerField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('USER_ID', 'USER_NAME', 'PHONE_NUMBER', 'EMAIL', 'MOVIE_NAME', 'SEATS')
     
     admin.py
     from django.contrib import admin
     from .models import Employee,EmployeeAdmin
     admin.site.register(Employee,EmployeeAdmin)

```

## OUTPUT
![alt text](<Screenshot 2025-04-13 215325.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
