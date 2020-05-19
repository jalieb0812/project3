# Generated by Django 2.2.10 on 2020-05-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_Platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter type of Dinner Platter', max_length=36, verbose_name='Dinner Platters')),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter Diiner Platter price', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of the extra', max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Enter price of the extra', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Pizza', 'Pizza'), ('Pasta', 'Pasta'), ('Subs', 'Subs'), ('Salad', 'Salad'), ('Dinner_Platter', 'Dinner_Platter'), ('Topping', 'Topping'), ('Extra', 'Extra'), ('Dessert', 'Dessert'), ('Pastry', 'Pastry'), ('Main', 'Main'), ('Appetizer', 'Appetizer'), ('Side', 'Side'), ('Miscellaneous', 'Miscellaneous')], help_text='Enter the category of the menu item', max_length=1, null=True)),
                ('name', models.CharField(help_text='Enter name of the menu item', max_length=128)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sizes', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra_Large')], help_text='Enter the allowable sizes of the menu item', max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter pasta type', max_length=36, verbose_name='Pasta Type')),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter pasta price', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter salad type', max_length=36, verbose_name='Salad Type')),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter salad price', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter sub type', max_length=36, verbose_name='Sub Type')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra_Large')], help_text='Enter sub size', max_length=1)),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter sub price', max_digits=4)),
                ('extras', models.ManyToManyField(related_name='sub_extra', to='orders.Extras', verbose_name='Extras')),
            ],
        ),
        migrations.CreateModel(
            name='Sicilian_Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra_Large')], help_text='Enter pizza size', max_length=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('num_toppings', models.IntegerField(default=0)),
                ('toppings', models.ManyToManyField(related_name='Sic_toppings', to='orders.Toppings', verbose_name='Toppings')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra_Large')], help_text='Enter pizza size', max_length=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('num_toppings', models.IntegerField(default=0)),
                ('toppings', models.ManyToManyField(related_name='reg_toppings', to='orders.Toppings', verbose_name='Toppings')),
            ],
        ),
    ]
