# Generated by Django 5.0.4 on 2024-04-11 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicines.departments', verbose_name='Отдел')),
            ],
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Скидка')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('description', models.TextField(verbose_name='Описание')),
                ('instruction', models.TextField(verbose_name='Инстукция')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicines.departments', verbose_name='Категория')),
            ],
        ),
    ]
