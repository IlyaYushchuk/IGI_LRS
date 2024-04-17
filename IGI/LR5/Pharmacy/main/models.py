from django.db import models
from django.utils import timezone

class New(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Заголовок')
    some_info = models.TextField(max_length=1000, verbose_name = 'Краткая информация')
    text = models.TextField(max_length=2000, verbose_name = 'Текст новости')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение', upload_to='medicines_images/')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
    
class Vacancy(models.Model):
    position = models.CharField(max_length=200, verbose_name = 'Должность')
    salary = models.PositiveIntegerField(default=0, verbose_name='Заработная плата')
    some_info = models.TextField(max_length=1000, verbose_name = 'Описание должности')
    city = models.CharField(max_length=30, verbose_name = 'Город')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.position
    
class Promotion(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Название')
    date = models.DateField(default=timezone.now(), verbose_name='Дата окончания', auto_now=False, auto_now_add=False)
    some_info = models.TextField(max_length=1000, verbose_name = 'Описание акции')
    discount = models.PositiveIntegerField(default=0, verbose_name = 'Скидка')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.title