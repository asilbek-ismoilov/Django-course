from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)  # Talabaning ismi
    last_name = models.CharField(max_length=100)   # Talabaning familiyasi
    age = models.IntegerField()                    # Yoshi
    email = models.EmailField(unique=True)         # Email
    joined_date = models.DateTimeField(auto_now_add=True)  # Qo‘shilgan sana

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# CharField() — Maksimum uzunligi cheklangan matn maydoni.
# IntegerField() — Butun son qiymatlarni saqlaydi.
# EmailField() — Faqat email manzillarni qabul qiladi.
# DateTimeField(auto_now_add=True) — Avtomatik ravishda hozirgi vaqtni saqlaydi.
# __str__ metodi modelning string ko‘rinishini qaytaradi.