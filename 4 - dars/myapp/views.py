from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'home.html')

def student_list(request):
    students = Student.objects.all()  # Barcha talabalarni olish
    return render(request, 'students.html', {'students': students})
