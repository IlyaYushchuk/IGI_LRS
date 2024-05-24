from django.db import models
from django.utils import timezone

from users.models import User, Master

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    text = models.TextField(max_length=2000, verbose_name = 'Текст новости')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение', upload_to='medicines_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Question(models.Model):
    question = models.TextField(max_length=2000, unique=True, verbose_name='Вопрос')
    answer = models.TextField(max_length=2000, verbose_name='Ответ', null=True, blank=True, default='На этот вопрос пока нет ответа.')
    date = models.DateField(default=timezone.now(), verbose_name='Дата добавления вопроса', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'

    def __str__(self):
        return self.question

class Vacancy(models.Model):
    position = models.CharField(max_length=200, verbose_name = 'Должность')
    salary = models.PositiveIntegerField(default=0, verbose_name='Заработная плата')
    some_info = models.TextField(max_length=1000, verbose_name = 'Описание должности')
    city = models.CharField(max_length=30, verbose_name = 'Город')
    
    def __str__(self):
        return self.position
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class Review(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Отзыв')
    rating = models.PositiveIntegerField(default=5, verbose_name='Оценка')
    date = models.DateTimeField(default=timezone.now(), verbose_name='Дата добавления отзыва', auto_now=False, auto_now_add=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Coupon(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Название')
    code = models.CharField(max_length=50, unique=True, verbose_name='Код')
    date = models.DateField(default=timezone.now(), verbose_name='Дата окончания', auto_now=False, auto_now_add=False)
    some_info = models.TextField(max_length=1000, verbose_name = 'Описание купона')
    discount = models.PositiveIntegerField(default=0, verbose_name = 'Скидка в %')

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return self.title
   