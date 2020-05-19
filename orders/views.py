from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Topping, Menu_Item

# Create your views here.
def index(request):

    context ={

        "Menu_Item": Menu_Item.objects.all(),

        "Pizza": Pizza.objects.all(),
        "rtoppings": Topping.rtoppings,
        "Toppings": Topping.objects.all(),


    }
    return render(request, "orders/index.html", context)
