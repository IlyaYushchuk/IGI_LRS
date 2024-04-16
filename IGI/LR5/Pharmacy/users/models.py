from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=19)
    image = models.ImageField(blank=True, null=True, verbose_name='Аватар', upload_to='users_images/')
    surname = models.CharField(max_length=150, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username