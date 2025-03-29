from django.shortcuts import render
from .models import *

def home(request):
    descriptions = Description.objects.all()
    portfolios = Portfolio.objects.all()
    context = {
        "descriptions": descriptions, 
        "portfolios": portfolios
    }

    return render(request, 'index.html', context)
