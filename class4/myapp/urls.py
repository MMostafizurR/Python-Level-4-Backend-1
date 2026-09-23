from django.urls import path
from myapp.views import *


urlpatterns = [
    path('home/', home, name='home'),
    path('addstudent/', add_student, name='addstudent'),
    path('editstudent/<int:student_id>/', edit_student, name='editstudent'),
    path('deletestudent/<int:student_id>/', delete_student, name='deletestudent'),
]