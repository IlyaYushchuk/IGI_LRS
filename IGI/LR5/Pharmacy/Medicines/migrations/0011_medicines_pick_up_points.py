# Generated by Django 5.0.4 on 2024-05-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicines', '0010_providers'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicines',
            name='pick_up_points',
            field=models.TextField(blank=True, null=True, verbose_name='Точки самовывоза'),
        ),
    ]
