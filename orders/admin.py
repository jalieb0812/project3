from django.contrib import admin


from .models import (Menu_Item, Topping, Extras, Pizza, Sicilian_Pizza,
Subs, Pasta, Salad, Dinner_Platter, Order, OrderItem, Profile, Items )


admin.site.register(Menu_Item)
admin.site.register(Topping)
admin.site.register(Extras)
admin.site.register(Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(Items)
