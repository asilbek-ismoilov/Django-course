from django.db import models

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

