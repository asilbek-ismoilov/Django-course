from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)   
    age = models.IntegerField()               
    email = models.EmailField(unique=True)    
    joined_date = models.DateTimeField(auto_now_add=True)  # Qo‘shilgan sana

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
