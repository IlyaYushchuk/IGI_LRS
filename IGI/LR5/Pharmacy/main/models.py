from django.db import models

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