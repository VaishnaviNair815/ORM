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
