from django.db import models

class About(models.Model):
    name = models.CharField(verbose_name = "Name", max_length=50)
    phone = models.CharField(verbose_name = "Phone", max_length=50)
    email = models.CharField(verbose_name = "Email", max_length=50)
    location = models.CharField(verbose_name = "Location", max_length=50)
    description = models.CharField(verbose_name = "Description", max_length=100)
    text = models.TextField(verbose_name = "Text")
    first_number = models.IntegerField(verbose_name = "First number")
    first_text = models.CharField(verbose_name = "First number text", max_length=50)
    second_number = models.IntegerField(verbose_name = "Second number")
    second_text = models.CharField(verbose_name = "Second number text", max_length=50)
    third_number = models.IntegerField(verbose_name = "Third number")
    third_text = models.CharField(verbose_name = "Third number text", max_length=50)

    def __str__(self):
        return f"{self.description} {self.location}"


class Resume(models.Model):
    name = models.CharField(verbose_name = "Name", max_length=100)
    text = models.CharField(verbose_name = "Text", max_length=200)

    def __str__(self):
        return f"{self.name}"
