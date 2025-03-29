from django.db import models

class Tools(models.Model):
    name = models.CharField(verbose_name = "Name", max_length=50)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.name}"
    

class Clients(models.Model):
    name = models.CharField(verbose_name = "Client name", max_length=50)
    work = models.CharField(verbose_name = "Work", max_length=100)
    for_work = models.CharField(verbose_name = "For work", max_length=100)
    text = models.TextField(verbose_name = "Text")

    def __str__(self):
        return f"{self.name}" 

