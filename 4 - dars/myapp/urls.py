from django.urls import path
from .views import home, student_list

urlpatterns = [
    path('',home,name='home-page'),
    path('students/', student_list, name='students')
]
