from django.db import models

class Contact(models.Model):
    name = models.CharField(verbose_name = "Name", max_length=50)
    email = models.CharField(verbose_name = "Email", max_length=50)
    phone_number = models.CharField(verbose_name = "Phone number", max_length=50)
    company = models.CharField(verbose_name = "Company name", max_length=10)
    text = models.TextField(verbose_name = "Text")

    def __str__(self):
        return f"{self.name} {self.phone_number}"