# Generated by Django 5.0.6 on 2024-05-23 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0014_alter_order_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateField(default=datetime.datetime(2024, 5, 23, 17, 3, 11, 962290, tzinfo=datetime.timezone.utc), verbose_name='Дата заказа'),
        ),
    ]
