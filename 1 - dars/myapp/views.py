from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Salom, bu mening birinchi Django sahifam!")
