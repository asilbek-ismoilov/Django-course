from django.db import models

class ProjectCategory(models.Model):
    category = models.CharField(verbose_name = "Category", max_length=100)

    def __str__(self):
        return f"{self.category}"


class Project(models.Model):
    name = models.CharField(verbose_name = "Project name", max_length=100)
    description = models.CharField(verbose_name = "Project description", max_length=100) 
    img = models.ImageField(upload_to='images/')
    category = models.ManyToManyField(ProjectCategory)

    def __str__(self):
        return f"{self.name}"

