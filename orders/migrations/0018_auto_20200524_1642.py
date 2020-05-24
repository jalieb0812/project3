# Generated by Django 2.2.10 on 2020-05-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_order_orderitem_profile_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
    ]