from django.contrib import admin
from .models import *

# from .models import Description, PortfolioCategory, Portfolio, About, ProjectCategory, Project, Resume, Edu, Experience, Tools, Clients, Contact

admin.site.register([
    Description, PortfolioCategory, Portfolio, About, 
    ProjectCategory, Project, Resume, Edu, Experience, 
    Tools, Clients, Contact
])

