# Generated by Django 5.0.4 on 2024-04-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='medicines_images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='new',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]
