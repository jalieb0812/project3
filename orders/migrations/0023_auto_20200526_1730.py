# Generated by Django 2.2.10 on 2020-05-26 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_orderitem_ptoppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='ptoppings',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pizza_toppings', to='orders.Menu_Item'),
        ),
    ]
