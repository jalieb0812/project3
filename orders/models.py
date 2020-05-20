from django.db import models

# Create your models here.
#you can also run python manage.py check; this checks for any problems in
#your project without making migrations or touching the database.

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

    category = models.CharField(max_length=36, null=True, blank=True, choices=MENU_CATEGORIES,
                                help_text='Enter the category of the menu item')

    name = models.CharField(max_length=128, help_text='Enter name of the menu item')

    price = price =  models.DecimalField(max_digits=4, null=True, blank=True, decimal_places=2)

    sizes = models.CharField(max_length=4, null=True, blank=True, choices=SIZE_CATEGORIES,
                                help_text='Enter the allowable sizes of the menu item')


    def __str__(self):
        return f" Category:{self.category} - Name:{self.name} - Sizes:{self.sizes} - Price: {self.price}"

class Topping(models.Model):
    topping_name = models.CharField(max_length=36)

    def __str__(self):
        return f"{self.topping_name}"

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

    toppings = models.ManyToManyField(Topping, related_name = "rpizza_toppings",  blank=True)

    #total_price= price + topping_price

    def __str__(self):
        return f" R_Pizza id: {self.id} - Item:{self.name} Size:{self.size} Number of toppings: {self.num_toppings}; \
        price$: {self.price}"


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

    toppings = models.ManyToManyField(Topping, related_name = "spizza_toppings",  blank=True)

    def __str__(self):
        return f" S_pizza id: {self.id} - Item{self.name} Size:{self.size}; Number of toppings {self.num_toppings}; \
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

    sub_extras = models.ManyToManyField(Extras,  blank=True, related_name="sub_extra") #verbose name =Sub extras

    def __str__(self):
        return f" Sub id: {self.id} - Sub:{self.name}- Size:{self.size}  price$: {self.price}"


class Pasta(models.Model):

    name = models.CharField("Pasta Type", max_length=36, help_text='Enter pasta type')
    price = models.DecimalField(max_digits=4,decimal_places=2, help_text='Enter pasta price')
    #type =
    def __str__(self):
        return f" Pasta id: {self.id} - Pasta_type: {self.name} price$: {self.price}"

class Salad(models.Model):

    name = models.CharField("Salad Type", max_length=36, help_text='Enter salad type')
    price = models.DecimalField(max_digits=4,decimal_places=2, help_text='Enter salad price')
    #type =
    def __str__(self):
        return f" Salad id: {self.id} - Salad_type: {self.name} price$: {self.price}"

class Dinner_Platter(models.Model):

    name = models.CharField("Dinner Platters", max_length=36, help_text='Enter type of Dinner Platter')
    price = models.DecimalField(max_digits=4,decimal_places=2, help_text='Enter Diiner Platter price')
    #type =
    def __str__(self):
        return f" Dinner Platter id: {self.id} - Dinner_Platter_type: {self.name} price$: {self.price}"
