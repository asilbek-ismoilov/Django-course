from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login # Foydalanuvchini tekshirish va tizimga kiritish uchun
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Ro‘yxatdan o‘tganidan keyin avtomatik login qilamiz
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

# is_valid() metodi orqali forma to‘g‘ri to‘ldirilganligini tekshiramiz. Agar foydalanuvchi noto‘g‘ri ma’lumot kiritgan bo‘lsa, funksiya pastdagi kodni bajarmaydi.


# set_password() metodi orqali parolni shifrlangan shaklda saqlaymiz.
# Agar oddiy .password = form.cleaned_data['password'] ishlatsak, parol oddiy matn sifatida saqlanadi va bu xavfsizlik nuqtai nazaridan xato hisoblanadi.


def user_login(request):
    if request.method == "POST":  # Agar foydalanuvchi formani yuborgan bo‘lsa
        username = request.POST.get('username')  # Foydalanuvchi nomini olish
        password = request.POST.get('password')  # Parolni olish
        user = authenticate(request, username=username, password=password)  # Foydalanuvchini tekshirish
        if user:  # Agar foydalanuvchi mavjud bo‘lsa
            login(request, user)  # Tizimga kiritish
            return redirect('home')  # Bosh sahifaga yo‘naltirish
        else:
            error_message = "Login yoki parol noto‘g‘ri!"  # Xatolik xabari
            return render(request, 'login.html', {'error_message': error_message})  # Xatolikni sahifaga jo‘natish
    
    return render(request, 'login.html')  # Login sahifasini chiqarish

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')