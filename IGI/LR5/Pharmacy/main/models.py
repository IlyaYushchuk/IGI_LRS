from django.db import models

class New(models.Model):
    title = models.CharField(max_length=30)
    some_info = models.CharField(max_length=100)
    text = models.CharField(max_length=300)