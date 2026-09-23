from django.shortcuts import redirect, render

from myapp.models import Student, Teachers

# Create your views here.

def home(request):

    teachers=Teachers.objects.all()
    students=Student.objects.all()

    for teacher in teachers:
        print(teacher.name, teacher.email, teacher.subject)

    for student in students:
        print(student.name, student.email, student.roll_number)


    context = {
        'student_name': 'Munna',
        'course_name': 'Python Level 4',
        'address': 'Dhaka, Bangladesh',
        'teachers': teachers,
        'students': students,
    }
    return render(request, 'index.html', context)

def add_student(request):
    students = Student.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll_number = request.POST.get('roll_number')
        image = request.FILES.get('image')

        student = Student(name=name, email=email, roll_number=roll_number, image=image)
        student.save()

        return redirect('home')
    return render(request, 'addstudent.html', {'students': students})

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.roll_number = request.POST.get('roll_number')
        student.image = request.FILES.get('image')
        student.save()
        return redirect('home')
    return render(request, 'editstudent.html', {'student': student})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('home')

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

