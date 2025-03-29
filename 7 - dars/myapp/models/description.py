from django.db import models


class Description(models.Model):
    first_name = models.CharField(verbose_name = "Name", max_length=50)
    last_name = models.CharField(verbose_name = "Surname", max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(verbose_name = "Description", max_length=100) 
    specialization = models.CharField(verbose_name = "Specialization", max_length=100)
    based_in = models.CharField(verbose_name = "Based in", max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.based_in}"

