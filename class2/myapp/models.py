from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name