from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['first_name', 'last_name', 'age', 'email']


# forms.ModelForm — Modeldan formani avtomatik yaratadi.
# Create - Yangi ma’lumot qo‘shish

# Django’da class Meta maxsus klass bo‘lib, u model yoki forma haqida qo‘shimcha ma’lumot (metadata) saqlash uchun ishlatiladi. 
# Bu Django modeli yoki formasining ishlash qoidalarini belgilash imkonini beradi.

# Meta klassi asosan Django Model va ModelForm larida ishlatiladi.

# model = Student – Qaysi model asosida forma yaratilishini bildiradi.
# fields = ['name', 'email', 'age'] – Qaysi maydonlar formaga kiritilishi kerakligi