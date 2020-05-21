from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Pizza, Topping, Menu_Item, Pasta, Subs, Salad, Dinner_Platter, Extras

# Create your views here.

#@login_required(login_url='login')
def index(request):

    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})



    menu_items = Menu_Item.objects.all()

    categories =  ["Pizza", "Pasta", "Subs", "Salad", "Dinner_Plater", "Topping",
                  "Extra", "Dessert", "Pastry", "Main", "Appetizer", "Side", "Miscellaneous"]



    pizza_categories = Menu_Item.objects.filter(category__contains="Pizza")

    toppings = Menu_Item.objects.filter(category__contains="Topping")

    extras = Menu_Item.objects.filter(category__contains="Extra")

    sub_categories = Menu_Item.objects.filter(category__contains="Subs")

    salad_categories = Menu_Item.objects.filter(category__contains="Salad")

    dinner_platter_categories = Menu_Item.objects.filter(category__contains="Dinner_Platter")

    pasta_categories = Menu_Item.objects.filter(category__contains="Pasta")


    context ={

        "user": request.user,

        "categories": categories,

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


def register_view(request):

    if request.method == 'GET':
        return render(request, 'orders/register.html', {"message": None})

    user = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    password_confirmation = request.POST['confirm_password']

    """ validate credentials server side"""
    if not user:
        return render(request, 'orders/register.html', {"message": "No username."})
    if len(user) < 4:
        return render(request, 'orders/register.html', {"message": "Username should be longer than 4 characters."})
    if not email:
        return render(request, 'orders/register.html', {"message": "Please enter a Proper Email."})
    # Email validation required.
    if not password or not password_confirmation:
        return render(request, 'orders/register.html', {"message": "Please enter a valid password."})

    if password != password_confirmation:
        return render(request, 'orders/register.html', {"message": "Passwords don't match. Please re-enter passwords"})


    if len(password) < 4 or len(password_confirmation) < 4 :
        return render(request, 'orders/register.html', {"message": "Password must be at least 4 charachters long."})

    if User.objects.filter(email=email):
        return render(request, 'orders/register.html', {"message": "Hmmm. Another user already has that email. \
        Please enter a different email address."})

    try:
        User.objects.create_user(user, email, password)
    except:
        return render(request, 'orders/register.html', {"message": "Registration failed."})

    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    return HttpResponseRedirect(reverse('login'))



def login_view(request):

    if request.method == "GET":

        return render(request, "orders/login.html")



    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})



def logout_view(request):

    logout(request)

    return render(request, "orders/login.html", {"message": "Successfully logged out."})
