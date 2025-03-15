from django.urls import path
from .views import home, student_list, add_student, update_student, delete_student

urlpatterns = [
    path('',home,name='home-page'),
    path('students/', student_list, name='students'),
    path('students/add/', add_student, name='add_student'),
    path('students/update/<int:student_id>/', update_student, name='update_student'),
    path('students/delete/<int:student_id>/', delete_student, name='delete_student'),
]
