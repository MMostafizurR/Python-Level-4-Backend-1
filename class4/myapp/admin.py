from django.contrib import admin

from myapp.models import Student, Teachers

# Register your models here.

admin.site.register(Teachers)
admin.site.register(Student)