# Generated by Django 2.2.10 on 2020-05-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0034_auto_20200527_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]