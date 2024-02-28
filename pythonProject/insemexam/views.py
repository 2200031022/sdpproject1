from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})
