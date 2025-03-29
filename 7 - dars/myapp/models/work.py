from django.db import models

class Edu(models.Model):
    year = models.CharField(verbose_name = "Year", max_length=100)
    cours_name = models.CharField(verbose_name = "Cours name", max_length=100)
    course_by = models.CharField(verbose_name = "Course by", max_length=100)
    text = models.CharField(verbose_name = "Text", max_length=200)

    def __str__(self):  
        return f"{self.year} {self.cours_name}"


class Experience(models.Model):
    year = models.CharField(verbose_name = "Year", max_length=100)
    work_name = models.CharField(verbose_name = "Work name", max_length=100)
    agency = models.CharField(verbose_name = "Agency", max_length=100)
    text = models.CharField(verbose_name = "Text", max_length=200)

    def __str__(self):  
        return f"{self.year} {self.work_name}"
    