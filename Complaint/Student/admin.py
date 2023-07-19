from django.contrib import admin
from .models import Student
# Register your models here.


class Student_admin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","phone","password")

admin.site.register(Student,Student_admin)
