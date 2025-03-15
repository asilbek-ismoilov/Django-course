from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def home(request):
    return render(request, 'home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})



def add_student(request):
    if request.method == "POST":  # Agar foydalanuvchi formani yuborsa
        form = StudentForm(request.POST)  # POST (foydalanuvchi kiritgan) ma'lumotlarni olamiz
        if form.is_valid():  # Agar forma valid (to‘g‘ri to‘ldirilgan) bo'lsa 
            form.save()  # Bazaga saqlaymiz
            return redirect('students')  # Barcha talabalar 'students' sahifasiga yo‘naltiramiz
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form})


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('students')

    return render(request, 'delete_student.html', {'student': student})
