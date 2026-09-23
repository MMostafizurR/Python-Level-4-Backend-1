from django.db import models

# Create your models here.

class Teachers(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.subject}"

class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    roll_number = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.roll_number}"