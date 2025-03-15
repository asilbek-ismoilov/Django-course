from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email']


# forms.ModelForm — Modeldan formani avtomatik yaratadi.
# Create - Yangi ma’lumot qo‘shish