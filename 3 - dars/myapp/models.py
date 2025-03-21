from django.db import models

class Student(models.Model):
    first_name = models.CharField(verbose_name = "Ism" ,max_length=100) 
    last_name = models.CharField(max_length=100) 
    age = models.IntegerField()                    
    email = models.EmailField(unique=True)       
    joined_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# models.CharField(max_length=...) - Qisqa matn saqlash uchun ishlatiladi (masalan, ism, email, username). max_length parametri majburiy va u matn uzunligini belgilaydi.
# models.TextField() - Uzoq matnlar uchun ishlatiladi (masalan, blog posti, sharh). max_length parametri yo‘q, cheksiz matn saqlash mumkin.
# models.IntegerField() - Butun son (integer) saqlash uchun ishlatiladi.
# models.FloatField() - Haqiqiy son (float) saqlash uchun ishlatiladi.
# models.DecimalField(max_digits=..., decimal_places=...) - Aniqlik talab qilinadigan kasr sonlar uchun ishlatiladi (masalan, narx, foiz).
# models.BigIntegerField() - Juda katta butun sonlarni saqlash uchun ishlatiladi (64-bit integer).
# models.PositiveIntegerField() - Faqat musbat butun sonlarni saqlaydi.
# models.DateField(auto_now_add=True, auto_now=False) - Sana (YYYY-MM-DD) saqlash uchun ishlatiladi.
# models.TimeField() - Faqat vaqtni saqlash uchun ishlatiladi (HH:MM:SS).
# models.DateTimeField(auto_now_add=True, auto_now=False) - Sana va vaqtni birgalikda saqlaydi.
# models.BooleanField(default=False) - True yoki False qiymatni saqlash uchun ishlatiladi.
# models.FileField(upload_to='uploads/') - Foydalanuvchilar fayl yuklashi uchun ishlatiladi.
# models.ImageField(upload_to='images/') -  Faqat rasm fayllarini yuklash uchun ishlatiladi.
# models.EmailField() - Email manzillarni saqlash uchun ishlatiladi.
# models.URLField() - URL manzillarni saqlash uchun ishlatiladi.
# models.SlugField() - Slug (my-article-title) saqlash uchun ishlatiladi.

# 🔹 Bog‘lanish maydonlari (Relations Fields)
# models.ForeignKey(Model, on_delete=models.CASCADE) - Bir modelni boshqa model bilan bog‘lash uchun ishlatiladi (Many-to-One).
# models.OneToOneField(Model, on_delete=models.CASCADE) - Ikki model o‘rtasida 1:1 bog‘lanish yaratadi.
# models.ManyToManyField(Model) - Many-to-Many munosabatlar yaratish uchun ishlatiladi.


# verbose_name=None – Maydon uchun tushunarli nom berish. Admin panel va boshqa joylarda foydalanuvchilarga ko'rsatiladi. Agar None bo‘lsa, Django modeldagi maydon nomidan foydalanadi.
# name=None – Maydonning bazadagi nomi. Django avtomatik aniqlaydi, lekin kerak bo'lsa qo'lda berish mumkin.
# primary_key=False – Ushbu maydon asosiy kalit (Primary Key) bo'lishi kerakligini belgilaydi. (True bo'lsa, ushbu maydon PK bo'ladi.)
# max_length=None – CharField yoki TextField uchun maksimal uzunlikni belgilaydi.
# unique=False – True bo'lsa, bu maydondagi qiymatlar takrorlanmasligi kerak bo'ladi.
# blank=False – True bo'lsa, forma to'ldirishda bu maydonni bo'sh qoldirish mumkin bo'ladi.
# null=False – True bo'lsa, ma'lumotlar bazasida bu maydon NULL bo'lishi mumkin. (blank bilan farqi bor.)
# db_index=False – True bo'lsa, ushbu maydonga indeks qo'shiladi, bu qidiruv jarayonini tezlashtiradi.
# rel=None – ForeignKey yoki OneToOneField uchun bog‘langan modelni saqlaydi.
# default=NOT_PROVIDED – Maydon uchun standart qiymat belgilaydi. (NOT_PROVIDED bo'lsa, hech qanday standart qiymat yo‘q.)
# editable=True – False bo'lsa, ushbu maydon admin panel va formalar orqali o'zgartirilmaydi.
# serialize=True – Ushbu maydon serializers (masalan, Django Rest Framework) orqali JSON formatga o‘tkazilishi mumkinligini belgilaydi.
# unique_for_date=None – Agar qiymati berilsa, bu maydonning bir xil qiymati faqat bitta sana ichida ishlatilishi mumkin bo'ladi.
# unique_for_month=None – unique_for_date kabi, lekin faqat oy doirasida amal qiladi.
# unique_for_year=None – unique_for_date kabi, lekin faqat yil doirasida amal qiladi.
# choices=None – Maydonda qaysi qiymatlar bo'lishi mumkinligini aniqlaydi ([(1, "Birinchi"), (2, "Ikkinchi")] kabi).
# help_text="" – Admin panel va formalar uchun yordamchi matn qo'shadi.
# db_column=None – Ma'lumotlar bazasidagi ustun nomini belgilaydi (o'zgarishi oldini olish uchun).
# db_tablespace=None – Maydon uchun ma'lumotlar bazasida qaysi joy (tablespace) ishlatilishini belgilaydi.
# auto_created=False – Django tomonidan avtomatik yaratilgan maydon yoki yo‘qligini bildiradi.
# validators=() – Maxsus tekshiruv (validation) funksiyalarini qo‘shish uchun ishlatiladi.
# error_messages=None – Xatolik yuz berganda chiqariladigan maxsus xabarlarni o'zgartirish uchun ishlatiladi.
# db_comment=None – Maydon haqida SQL bazada izoh (COMMENT) qo'shish uchun ishlatiladi.


# __str__ metodi modelning string ko‘rinishini qaytaradi. bu kodni maqsadi, 
# modelni admin panelida ko‘rsatish uchun string ko‘rinishini qaytarish.
