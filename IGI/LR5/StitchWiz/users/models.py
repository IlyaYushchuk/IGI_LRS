from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True,null=True)
    phone = models.CharField(max_length=19,blank=True, null=True)
    position = models.CharField(max_length=150, blank=True, null=True)
    
    is_master = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

class Master(User):
    
    def __str__(self):
        return super().username
    
    class Meta:
        db_table = 'master'
        verbose_name = 'Мастера'
        verbose_name_plural = 'Мастеры'