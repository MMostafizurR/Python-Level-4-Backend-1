from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'student_name': 'Munna',
        'course_name': 'Python Level 4 Backend',
        'status': 'Active',
    }
    return render(request, 'index.html', context)