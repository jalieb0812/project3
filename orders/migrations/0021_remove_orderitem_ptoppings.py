# Generated by Django 2.2.10 on 2020-05-26 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_orderitem_ptoppings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='ptoppings',
        ),
    ]