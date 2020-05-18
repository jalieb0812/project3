from django.db import models

# Create your models here.

class Toppings(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"

class Pizza(models.Model):

    name = "Regular Pizza"

    size = models.CharField(max_length=10) #maybe extra Large
    price = models.IntegerField(blank=True, default=0)
    #topings = model.
    num_toppings = models.IntegerField(blank=True, default=0)
    reg_toppings = models.ForeignKey(Toppings, on_delete=models.CASCADE, related_name="Reg_extras")

    def __str__(self):
        return f" Item:{self.name} Size:{self.size} Number of toppings: {self.num_toppings}; \
        toppings {self.reg_toppings} cost$: {self.price}"


class Sicilian_Pizza(models.Model):

    name = "Sicilian Pizza"
    

    size = models.CharField(max_length=10) #maybe extra Large
    price = models.IntegerField(blank=True, default=0)
    num_toppings = models.IntegerField(blank=True, default=0)
    sic_toppings = models.ForeignKey(Toppings, default=1, on_delete=models.CASCADE, related_name="Sic_extras")

    def __str__(self):
        return f" Item{self.name} Size:{self.size}; Number of toppings {self.num_toppings}; \
        toppings: {self.sic_toppings}; cost$: {self.price}"



class Subs(models.Model):
    size = models.CharField(max_length=10) #maybe extra Large
    price = models.IntegerField()
    #type =
    #extras =

    def __str__(self):
        return f"{self.size}  cost$: {self.price}"

class Sub_Types(models.Model):
    sub_type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.sub_type}"


class Sub_Extras(models.Model):
    sub_extra = models.CharField(max_length=64)
    num_extras = models.IntegerField()
    def __str__(self):
        return f"{self.sub_extra} - {self.num_extras}"

class Pasta(models.Model):
    price = models.IntegerField()
    #type =
    def __str__(self):
        return f"cost$: {self.price}"

class Salad(models.Model):
    price = models.IntegerField()
    #type =
    def __str__(self):
        return f" cost$: {self.price}"

class Dinner_Platter(models.Model):

    size = models.CharField(max_length=10) #maybe extra Large
    price = models.IntegerField()
    #type =
    def __str__(self):
        return f"{self.size}  cost$: {self.price}"
