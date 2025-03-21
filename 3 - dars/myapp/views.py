from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'home.html')

def student_list(request):
    students = Student.objects.all()  
    return render(request, 'students.html', {'students': students})

# Django ORM (objects) 

# .all() - Barcha yozuvlarni olib keladi.
# students = Student.objects.all()


# .filter(**kwargs) - Ma’lumotlarni shart bo‘yicha filtrlash uchun ishlatiladi.
# students = Student.objects.filter(age=20)  # 20 yoshli talabalar


# .exclude(**kwargs) - Berilgan shartga mos kelmaydigan obyektlarni chiqarib tashlaydi.
# students = Student.objects.exclude(age=20)  # 20 yoshli talabalar bundan mustasno


# .get(**kwargs) - Bitta natija olish uchun ishlatiladi (agar natija 2 yoki undan ko‘p bo‘lsa, xato beradi).
# student = Student.objects.get(id=1)  # ID=1 bo'lgan talabani olib keladi
# ⚠️ Eslatma: Agar id=1 yo‘q bo‘lsa, DoesNotExist xatosi keladi. Agar bir nechta natija bo‘lsa, MultipleObjectsReturned xatosi bo‘ladi.


# .order_by('field_name') - Ma’lumotlarni saralash uchun ishlatiladi.
# students = Student.objects.order_by('name')  # Ism bo‘yicha alfavit tartibida
# students = Student.objects.order_by('-age')  # Yosh bo‘yicha teskari tartibda


# .values(*fields) - Ma’lumotlarni lug‘at (dict) sifatida qaytaradi.
# students = Student.objects.values('name', 'age')  
# Natija: [{'name': 'Ali', 'age': 20}, {'name': 'Aziz', 'age': 22}]


# .values_list(*fields, flat=True) - values_list() faqat kerakli ustunlarni olib keladi.
# names = Student.objects.values_list('name', flat=True)
# Natija: ['Ali', 'Aziz']


# .count() - Ma’lumotlar sonini qaytaradi | Umumiy yozuvlar sonini qaytaradi
# total_students = Student.objects.count()


# .exists() - Natija bor yoki yo‘qligini tekshiradi (True yoki False).
# has_students = Student.objects.filter(age=20).exists() # - Agar hech narsa topilmasa, False, aks holda True.


# .first() va .last() - Birinchi yoki oxirgi yozuvni olib keladi.
# first_student = Student.objects.first()
# last_student = Student.objects.last()


# .distinct() - Takrorlanadigan yozuvlarni olib tashlaydi
# students = Student.objects.values('age').distinct()  # Unikal yoshlar


# .reverse() - Saralash tartibini teskari qiladi (order_by bilan ishlatiladi).
# students = Student.objects.order_by('name').reverse()


# .update(**kwargs) - Bir yoki bir nechta yozuvni yangilaydi.
# Student.objects.filter(id=1).update(name="Muhammad")


# .delete() - Ma’lumotlarni o‘chirish uchun ishlatiladi.
# Student.objects.filter(age=20).delete()  # 20 yoshli barcha talabalarni o‘chirish
