from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')
    department = models.ForeignKey(to=Departments, on_delete=models.CASCADE, verbose_name='Отдел')

class Medicines(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='URL')
    category = models.ForeignKey(to=Departments, on_delete=models.CASCADE, verbose_name='Категория')
    discount = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Скидка')
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    description = models.TextField(verbose_name='Описание')
    instruction = models.TextField(verbose_name='Инстукция')