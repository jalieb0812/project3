from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
User = get_user_model()


#from django.db.models.signals import post_save

#from django.contrib.auth import get_user_model

#User = get_user_model()

#from products.models import Product

#import stripe

#stripe.api_key = settings.STRIPE_SECRET_KEY

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
    ('Sm', 'Small'),
    ('Md', 'Medium'),
    ('Lg', 'Large'),
    ('XL', 'Extra_Large')
    )

    category = models.CharField(max_length=36, null=True, blank=True, choices=MENU_CATEGORIES,
                                help_text='Enter the category of the menu item')

    name = models.CharField(max_length=128, help_text='Enter name of the menu item')

    price =  models.DecimalField(max_digits=4, null=True, blank=True, decimal_places=2, default=0.00)

    sizes = models.CharField(max_length=4, null=True, blank=True, choices=SIZE_CATEGORIES,
                                help_text='Enter the allowable sizes of the menu item')

    toppings = models.CharField( max_length=400, blank=True, null=True, help_text='Enter toppings')
    num_toppings = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return f" Category:{self.category} - Name:{self.name} - Sizes:{self.sizes} - Price: {self.price} \
        -numtoppings {self.num_toppings} - toppings {self.toppings}"



class Topping(models.Model):
    topping_name = models.CharField(max_length=36)
    price = models.DecimalField(max_digits=4, null=True, blank=True, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.topping_name}"

class Extras(models.Model):
    name = models.CharField(max_length=64, help_text='Enter name of the extra')
    price = models.DecimalField(max_digits=4,decimal_places=2, default=0, help_text='Enter price of the extra')

    def __str__(self):
        return f"{self.name} - {self.price}"

"""
class Pizza_Item(Menu_Item):

    toppings = models.ManyToManyField(Topping, blank=True, help_text='Enter toppings')
    num_toppings = models.IntegerField(default=0)


    def __str__(self):
        return f" Category:{self.category} - Name:{self.name} - Sizes:{self.sizes} \
         - Price: {self.price} -numtoppings {self.num_toppings} - toppings {self.toppings}"
"""

class Items(models.Model):

    category = models.CharField(max_length=36, null=True, blank=True, help_text='Enter the category of the menu item')

    name = models.CharField(max_length=128, help_text='Enter name of the menu item')

    price = price =  models.DecimalField(max_digits=4, null=True, blank=True, decimal_places=2)

    sizes = models.IntegerField( null=True, blank=True,  help_text='Enter the allowable sizes of the menu item')


    def __str__(self):
        return f" Category:{self.category} - Name:{self.name} - Sizes:{self.sizes} - Price: {self.price}"




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

    price =  models.DecimalField(max_digits=4,decimal_places=2, default=0.00)
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


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(Menu_Item, blank=True)
    #stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        user_profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

class OrderItem(models.Model):
    menu_item = models.ForeignKey(Menu_Item,on_delete=models.CASCADE, blank=True, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    is_topping =models.BooleanField(default=False)
    #quantity = models.IntegerField(default=1)
    num_extras = models.IntegerField( blank=True, default=0)

    extras = models.CharField(max_length=400,  blank=True, null=True)

    extras_cost = models.DecimalField(max_digits=4,decimal_places=2, default = 0.00)

    ptoppings = models.CharField(max_length=400,  blank=True, null=True)
    def __str__(self):
        return f"{self.menu_item} - {self.date_added} - status:{self.is_ordered} \
         - {self.date_ordered}- {self.is_topping} - Num extras:{self.num_extras} \
         - sub_extras {self.extras}"


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    ordered_items = models.ManyToManyField(OrderItem)
    # payment_details = models.ForeignKey(Payment, null=True)
    date_ordered = models.DateTimeField(auto_now=True)

    # reutrn number of ordered items.
    def num_order_items(self):
        return self.order_items.count()

    #get all the orders ordered_items
    def get_cart_ordered_items(self):
        return self.ordered_items.all()
        #exclude(is_topping=True)

    def get_cart_ordered_items_toppings(self):
        return self.ordered_items.all()
        #sum of total price of all ordered_items

    def get_cart_total(self):

    #    Extra = Menu_Item.objects.filter(name="Sub_Extra")



        return sum([item.menu_item.price for item in self.ordered_items.all()]
        + [item.extras_cost for item in self.ordered_items.all()])
        #.exclude(is_topping=True)])





    def __str__(self):
        return f"{self.owner} - {self.ordered_items.all()} - {self.date_ordered}"
        #return '{0} - {1}'.format(self.owner, self.ref_code)
