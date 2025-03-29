from django.db import models


class Description(models.Model):
    name = models.CharField(verbose_name = "Name", max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(verbose_name = "Description", max_length=100) 
    specialization = models.CharField(verbose_name = "Specialization", max_length=100)
    based_in = models.CharField(verbose_name = "Based in", max_length=100)

    def __str__(self):
        return f"{self.name} {self.based_in}"


class PortfolioCategory(models.Model):
    category = models.CharField(verbose_name = "Category", max_length=100)

    def __str__(self):
        return f"{self.category}"


class Portfolio(models.Model):
    name = models.CharField(verbose_name = "Portfolio name", max_length=100)
    description = models.CharField(verbose_name = "Portfolio description", max_length=100) 
    img = models.ImageField(upload_to='images/')
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.category}"


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


class Resume(models.Model):
    name = models.CharField(verbose_name = "Name", max_length=100)
    text = models.CharField(verbose_name = "Text", max_length=200)

    def __str__(self):
        return f"{self.name}"


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


class Contact(models.Model):
    name = models.CharField(verbose_name = "Name", max_length=50)
    email = models.CharField(verbose_name = "Email", max_length=50)
    phone_number = models.CharField(verbose_name = "Phone number", max_length=50)
    company = models.CharField(verbose_name = "Company name", max_length=10)
    text = models.TextField(verbose_name = "Text")

    def __str__(self):
        return f"{self.name} {self.phone_number}"