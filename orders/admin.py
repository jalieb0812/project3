from django.contrib import admin

from .models import Pizza, Toppings, Sicilian_Pizza

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Sicilian_Pizza)
