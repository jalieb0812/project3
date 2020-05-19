from django.db import models

# Create your models here.

class Menu_Item(models.Model):

    MENU_CATEGORIES = (
    ('Pizza', 'Pizza'),
    ('Pasta', 'Pasta'),
    ('Subs', 'Subs'),
    ('Salad', 'Salad'),
    ('Dinner_Platter', 'Dinner_Platter'),
    ('Topping', 'Topping'),
    ('Extra', 'Extra'),
    ('Dessert', 'Dessert'),
    ('Pastry', 'Pastry'),
    ('Main', 'Main'),
    ('Appetizer', 'Appetizer'),
    ('Side', 'Side'),
    ('Miscellaneous', 'Miscellaneous')
    )

    SIZE_CATEGORIES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra_Large')
    )

    category = models.CharField(max_length=1, null=True, blank=True, choices=MENU_CATEGORIES,
                                help_text='Enter the category of the menu item')

    name = models.CharField(max_length=128, help_text='Enter name of the menu item')

    price = price =  models.DecimalField(max_digits=4, null=True, blank=True, decimal_places=2)

    sizes = models.CharField(max_length=4, null=True, blank=True, choices=SIZE_CATEGORIES,
                                help_text='Enter the allowable sizes of the menu item')


    def __str__(self):
        return f" Category:{self.category} - Name:{self.name} - Sizes:{self.size} - Price: {self.price}"

class Toppings(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self):
        return f"{self.name}"

class Extras(models.Model):
    name = models.CharField(max_length=64, help_text='Enter name of the extra')
    price = models.DecimalField(max_digits=4,decimal_places=2, default=0, help_text='Enter price of the extra')

    def __str__(self):
        return f"{self.name} - {self.price}"


class Pizza(models.Model):

    name = "Regular Pizza"

    SIZE_CATEGORIES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra_Large')
    )


    size = models.CharField(max_length=1, choices=SIZE_CATEGORIES,
                            help_text='Enter pizza size')

    price =  models.DecimalField(max_digits=4,decimal_places=2)
    #topings = model.

    num_toppings = models.IntegerField(default=0)

    toppings = models.ManyToManyField(Toppings, verbose_name="Toppings",  blank=True,  related_name="reg_toppings")

    #total_price= price + topping_price

    def __str__(self):
        return f" Item:{self.name} Size:{self.size} Number of toppings: {self.num_toppings}; \
        toppings {self.toppings} price$: {self.price}"


class Sicilian_Pizza(models.Model):

    name = "Sicilian Pizza"

    SIZE_CATEGORIES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra_Large')
    )


    size = models.CharField(max_length=1, choices=SIZE_CATEGORIES,
                            help_text='Enter pizza size')

    price =  models.DecimalField(max_digits=4,decimal_places=2)
    #topings = model.

    num_toppings = models.IntegerField(default=0)

    toppings = models.ManyToManyField(Toppings, verbose_name="Toppings",  blank=True, related_name="Sic_toppings")

    def __str__(self):
        return f" Item{self.name} Size:{self.size}; Number of toppings {self.num_toppings}; \
        toppings: {self.toppings}; price$: {self.price}"



class Subs(models.Model):

    name = models.CharField("Sub Type", max_length=36, help_text='Enter sub type')

    SIZE_CATEGORIES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra_Large')
    )

    size = models.CharField(max_length=1, choices=SIZE_CATEGORIES,
                            help_text='Enter sub size')


    price = models.DecimalField(max_digits=4,decimal_places=2, help_text='Enter sub price')

    extras = models.ManyToManyField(Extras, verbose_name="Extras",  blank=True,  related_name="sub_extra")

    def __str__(self):
        return f" Sub:{self.name}- Size:{self.size}  price$: {self.price}"


class Pasta(models.Model):

    name = models.CharField("Pasta Type", max_length=36, help_text='Enter pasta type')
    price = models.DecimalField(max_digits=4,decimal_places=2, help_text='Enter pasta price')
    #type =
    def __str__(self):
        return f" Pasta_type: {self.name} price$: {self.price}"

class Salad(models.Model):

    name = models.CharField("Salad Type", max_length=36, help_text='Enter salad type')
    price = models.DecimalField(max_digits=4,decimal_places=2, help_text='Enter salad price')
    #type =
    def __str__(self):
        return f" Salad_type: {self.name} price$: {self.price}"

class Dinner_Platter(models.Model):

    name = models.CharField("Dinner Platters", max_length=36, help_text='Enter type of Dinner Platter')
    price = models.DecimalField(max_digits=4,decimal_places=2, help_text='Enter Diiner Platter price')
    #type =
    def __str__(self):
        return f" Salad_type: {self.name} price$: {self.price}"
