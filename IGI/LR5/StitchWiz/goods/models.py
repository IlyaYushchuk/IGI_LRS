from django.db import models
from users.models import Master
from users.models import User, Master
from main_page.models import Coupon
from django.utils import timezone
from decimal import Decimal
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique= True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class   Products(models.Model):
    name = models.CharField(max_length=150, unique= True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name = 'Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')    

    masters = models.ManyToManyField(Master, related_name='masters')
    

    def __str__(self):
        return self.name
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price*(1-self.discount/100),2)
        return self.price 

    class Meta:
        ordering = ('id',)
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Order(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='Заказчик')    
    master = models.ForeignKey(to=Master, on_delete=models.PROTECT, related_name='Мастер')    
    date_order = models.DateField(default=timezone.now(), verbose_name='Дата заказа', auto_now=False, auto_now_add=False)
    date_release = models.DateField( blank=True, verbose_name='Дата отдачи заказа', auto_now=False, auto_now_add=False)

    is_released = models.BooleanField(default=False)
    is_processing = models.BooleanField(default=True)
    is_canceled = models.BooleanField(default=False)

    coupon = models.ForeignKey(to=Coupon, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Купон') 
    product = models.ForeignKey(to=Products, on_delete=models.PROTECT, verbose_name='Услуга') 
 

    comments = models.TextField(max_length=1000,blank=True, null=True, verbose_name = 'Комментарий')

    def get_price(self):
        if self.coupon:
            price = self.product.sell_price()
            return round(price*Decimal(1-self.coupon.discount/100),2)
        return self.product.sell_price()

    list_display = ('id', 'date_order')  # Поля для отображения в списке
    ordering = ('-date_order',)
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'