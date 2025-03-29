# Generated by Django 5.1.5 on 2025-03-24 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('text', models.TextField(verbose_name='Text')),
                ('first_number', models.IntegerField(verbose_name='First number')),
                ('first_text', models.CharField(max_length=50, verbose_name='First number text')),
                ('second_number', models.IntegerField(verbose_name='Second number')),
                ('second_text', models.CharField(max_length=50, verbose_name='Second number text')),
                ('third_number', models.IntegerField(verbose_name='Third number')),
                ('third_text', models.CharField(max_length=50, verbose_name='Third number text')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Client name')),
                ('work', models.CharField(max_length=100, verbose_name='Work')),
                ('for_work', models.CharField(max_length=100, verbose_name='For work')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Phone number')),
                ('company', models.CharField(max_length=10, verbose_name='Company name')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('specialization', models.CharField(max_length=100, verbose_name='Specialization')),
                ('based_in', models.CharField(max_length=100, verbose_name='Based in')),
            ],
        ),
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100, verbose_name='Year')),
                ('cours_name', models.CharField(max_length=100, verbose_name='Cours name')),
                ('course_by', models.CharField(max_length=100, verbose_name='Course by')),
                ('text', models.CharField(max_length=200, verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100, verbose_name='Year')),
                ('work_name', models.CharField(max_length=100, verbose_name='Work name')),
                ('agency', models.CharField(max_length=100, verbose_name='Agency')),
                ('text', models.CharField(max_length=200, verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('text', models.CharField(max_length=200, verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Portfolio name')),
                ('description', models.CharField(max_length=100, verbose_name='Portfolio description')),
                ('img', models.ImageField(upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.portfoliocategory')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Project name')),
                ('description', models.CharField(max_length=100, verbose_name='Project description')),
                ('img', models.ImageField(upload_to='images/')),
                ('category', models.ManyToManyField(to='myapp.projectcategory')),
            ],
        ),
    ]
