from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Pizza, Topping, Menu_Item

# Create your views here.
def index(request):

    menu_items = Menu_Item.objects.all()




    pizza_categories = Menu_Item.objects.filter(category__contains="Pizza")

    toppings = Menu_Item.objects.filter(category__contains="Topping")

    extras = Menu_Item.objects.filter(category__contains="Extra")

    sub_categories = Menu_Item.objects.filter(category__contains="Subs")

    salad_categories = Menu_Item.objects.filter(category__contains="Salad")

    dinner_platter_categories = Menu_Item.objects.filter(category__contains="Dinner_Platter")

    pasta_categories = Menu_Item.objects.filter(category__contains="Pasta")


    context ={


        "menu_item": menu_items,
        "pizza_categories": pizza_categories,
        "toppings": toppings,
        "extras": extras,
        "sub_categories": sub_categories,
        "salad_categories": salad_categories,
        "dinner_platter_categories": dinner_platter_categories,
        "pasta_categories": pasta_categories,

        "Pizza": Pizza.objects.all(),
        "pizza_toppings": Pizza.toppings,
        "Toppings": Topping.objects.all(),


    }
    return render(request, "orders/index.html", context)
