# Generated by Django 2.2.10 on 2020-05-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='rtoppings',
            field=models.ManyToManyField(default=None, to='orders.Topping', verbose_name='Toppings'),
        ),
        migrations.AlterField(
            model_name='sicilian_pizza',
            name='stoppings',
            field=models.ManyToManyField(default=None, to='orders.Topping', verbose_name='Toppings'),
        ),
    ]
