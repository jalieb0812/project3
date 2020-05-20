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






    context ={

        "menu_item": menu_items,
        "pizza_categories": pizza_categories,

        "Pizza": Pizza.objects.all(),
        "pizza_toppings": Pizza.toppings,
        "Toppings": Topping.objects.all(),


    }
    return render(request, "orders/index.html", context)
