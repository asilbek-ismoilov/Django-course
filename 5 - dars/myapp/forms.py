from django import forms  
from django.contrib.auth.models import User  # Foydalanuvchi modeli bilan ishlash uchun import qilamiz

class SignUpForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput)  # Parolni kiritish uchun maxsus input
    confirm_password = forms.CharField(widget=forms.PasswordInput)  # Parolni tasdiqlash uchun input

    class Meta:
        model = User  # Django ichki User modelidan foydalanamiz
        fields = ['username', 'email', 'password']  # Foydalanuvchi kiritishi kerak bo‘lgan maydonlar

    def clean(self):  # Formani tozalash (validatsiya qilish)
        cleaned_data = super().clean()  # Forma ma'lumotlarini olish
        password = cleaned_data.get("password")  # Asosiy parol
        confirm_password = cleaned_data.get("confirm_password")  # Tasdiqlash paroli

        if password and confirm_password and password != confirm_password:  # Agar parollar mos kelmasa
            raise forms.ValidationError("Parollar mos kelmadi!")  # Xatolikni chiqaramiz

        return cleaned_data  # Tozalangan ma’lumotlarni qaytaramiz
