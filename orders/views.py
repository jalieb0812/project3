from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

#from accounts.models import Profile

from .models import (Pizza, Topping, Menu_Item, Pasta, Profile,
Subs, Salad, Dinner_Platter, Extras, Order, OrderItem, Transaction, User)

import datetime

# Create your views here.

def profile(request):

    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)


    context = { 'my_orders': my_orders}

    return render(request, "orders/profile.html", context)

#@login_required(login_url='login')
def index(request):

    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})



    menu_items = Menu_Item.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []

    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.ordered_items.all() # warning 2 menu_items variables
        current_order_products = [menu_item.menu_item for menu_item in user_order_items]

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

        'current_order_products': current_order_products,

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


def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    menu_item = Menu_Item.objects.filter(id=kwargs.get('item_id', "")).first() #item id sent from the url

    """

    I dont need this
    # check if the user already owns this product
    if product in request.user.profile.ebooks.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('products:product-list'))
    """
    # create orderItem of the selected menu_item
    order_item, status = OrderItem.objects.get_or_create(menu_item=menu_item)

    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)

    user_order.ordered_items.add(order_item)

    #print(f"the are the current order products: {current_order_products}")


    if status:
    #not sure i care about generating a reference code. in extras.py
        # generate a reference code
        #user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    #messages.info(request, "item added to cart")


    return HttpResponseRedirect(reverse('orders:index'))


def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        #messages.info(request, "Item has been deleted")
    return redirect(reverse('orders:ordersummary'))

def customize_order(request, food, **kwargs):

    if request.method == "GET":

        menu_items = Menu_Item.objects.all()
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []

        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.ordered_items.all() # warning 2 menu_items variables
            current_order_products = [menu_item.menu_item for menu_item in user_order_items]



        toppings = Menu_Item.objects.filter(category__contains="Topping")

        extras = Menu_Item.objects.filter(category__contains="Extra")

        pizza_categories = Menu_Item.objects.filter(category__contains="Pizza")

        sub_categories = Menu_Item.objects.filter(category__contains="Subs")


        menu_items = Menu_Item.objects.all()

        ordered_item = Menu_Item.objects.filter(name=food).first()


        context ={

                "ordered_item": ordered_item,
                #"order_item_id": int(order_item.pk),

                "user": request.user,

                'current_order_products': current_order_products,

                "menu_item": menu_items,
                "pizza_categories": pizza_categories,
                "toppings": toppings,
                "extras": extras,
                "sub_categories": sub_categories,


            }
        return render(request, "orders/customize_order.html", context)



    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id

    menu_item = Menu_Item.objects.filter(name=food).first()
    print (f"this is menu item in get {menu_item}")

    toppings = []

    topping1 = request.POST["topping1"]
    toppings.append(topping1)

    try:
        topping2 = request.POST["topping2"]
        toppings.append(topping2)
    except MultiValueDictKeyError:
        toppings2 = False

    try:
        topping3 = request.POST["topping3"]
        toppings.append(topping3)

    except MultiValueDictKeyError:
        topping3 = False





    print(f"these are the toppings: {toppings}")




    #menu_item = Menu_Item.objects.f(pk=kwargs.get('item_id', "")).first() #item id sent from the url



    # create orderItem of the selected menu_item
    order_item, status = OrderItem.objects.get_or_create(menu_item=menu_item, ptoppings=toppings)

#    toppingsss, status = OrderItem.objects.get_or_create(ptoppings=toppings, is_topping=True)


    #total = OrderItem.objects.all().aggregate(sum('price')).values()

    #print (f"{total}")

    print (f"this is order_item item in get {order_item} \n")

    print (f"this is topings order item in get {toppings} \n")


    #order_item.toppings = topping
    print (f"this is order item item with toppings: {order_item}")


    #user_orderitem, status = OrderItem.objects.get_or_create( is_ordered=False)

    #user_orderitem.save()
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)

    user_order.ordered_items.add(order_item)
    #user_order.ordered_items.add(toppingsss)


    #print(f"the are the current order products: {current_order_products}")



    if status:
    #not sure i care about generating a reference code. in extras.py
        # generate a reference code
        #user_order.ref_code = generate_order_id()
        user_order.save()

    print (f"this is user order in get {user_order.ordered_items.all()}")





        #return render(request, "orders/customize_order.html", context)

    return HttpResponseRedirect(reverse('orders:index'))




    #    if request.method== "POST":


        #    toppings = request.form.get()

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders with is_ordered = false
        return order[0]
    return 0

def order_details(request, **kwargs):
    #user_profile = get_object_or_404(Profile, user=request.user)
    #current_order = Order.objects.filter (owner=user_profile, is_ordered=False)
    #orders = current_order[0]
    existing_order = get_user_pending_order(request)
    user_profile = get_object_or_404(Profile, user=request.user)

    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    print(f"{order} \n")



    itemss = Order.objects.filter(ordered_items__menu_item__name__icontains = "Pizza", is_ordered=False)
    print(f"theser are tehe itttees,{itemss} \n \n")

#    zzz=itemss.filter(ordered_items__menu_item__is_topping=True)

    print(f"theser are zzz,{itemss}")
    total = 0


    # for item in order:
    #     print(f"{item}")
    #     if item.menu_item.price != None:
    #         total += item.menu_item.price
    # print (f"total")


    context = {
        'order': existing_order,
        #'orders': orders
    }
    return render(request, 'orders/ordersummary.html', context)


def checkout(request, **kwargs):
    existing_order = get_user_pending_order(request)

    context = {
        'order': existing_order,
    }

    return render(request, 'orders/checkout.html', context)

def process_payment(request, order_id):
    # process payment; just using this as a way to pass in the order_id to checkout
    return redirect (reverse('orders:updaterecords',
                        kwargs= {
                            'order_id': order_id,
                        })
                        )

def updaterecords(request, order_id):
    # get the order being processed
    order_to_purchase = Order.objects.filter(pk=order_id).first()

    # update the placed order
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
    order_to_purchase.save()

    # get all ordered_items in the order - generates a queryset
    order_items = order_to_purchase.ordered_items.all()

    # update order items
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    # Add products to user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # get the products from the items / the ordderd products are eqaul to
    order_products = [item.menu_item for item in order_items]

    #adding ordered_products list of objects profiles menu_item field (to a many to many field)
    # the * iteates through all the objects in the list
    user_profile.menu_items.add(*order_products)
    user_profile.save()


    """
    # create a transaction
    transaction = Transaction(profile=request.user.profile,
                            token=token,
                            order_id=order_to_purchase.id,
                            amount=order_to_purchase.get_cart_total(),
                            success=True)
    # save the transcation (otherwise doesn't exist)
    transaction.save()
    """


    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    #messages.info(request, " Order complete! Thank you!")

    # redirects to users profiel so they can see the order
    return redirect(reverse('orders:success'))


def get_user_ordered_items(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=True)
    if order.exists():
        # get the only order in the list of filtered orders
        return order.last()
    return 0

# not sure i need this view.
def success(request, **kwargs):
    # a view signifying the transcation was successful
    finished_order = get_user_ordered_items(request)

    context = {
        'order': finished_order,
    }
    return render(request, 'orders/purchase_success.html', context)



# @login_required()
# def delete_from_cart(request, item_id):
#     item_to_delete = OrderItem.objects.filter(pk=item_id)
#     if item_to_delete.exists():
#         item_to_delete[0].delete()
#         messages.info(request, "Item has been deleted")
#     return redirect(reverse('shopping_cart:order_summary'))


# @login_required()
# def order_details(request, **kwargs):
#     existing_order = get_user_pending_order(request)
#     context = {
#         'order': existing_order
#     }
#     return render(request, 'shopping_cart/order_summary.html', context)
#
# def get_user_pending_order(request):
#     # get order for the correct user
#     user_profile = get_object_or_404(Profile, user=request.user)
#     order = Order.objects.filter(owner=user_profile, is_ordered=False)
#     if order.exists():
#         # get the only order in the list of filtered orders
#         return order[0]
#     return 0
#
# @login_required()
# def checkout(request, **kwargs):
#     client_token = generate_client_token()
#     existing_order = get_user_pending_order(request)
#     publishKey = settings.STRIPE_PUBLISHABLE_KEY
#     if request.method == 'POST':
#         token = request.POST.get('stripeToken', False)
#         if token:
#             try:
#                 charge = stripe.Charge.create(
#                     amount=100*existing_order.get_cart_total(),
#                     currency='usd',
#                     description='Example charge',
#                     source=token,
#                 )
#
#                 return redirect(reverse('shopping_cart:update_records',
#                         kwargs={
#                             'token': token
#                         })
#                     )
#             except stripe.CardError as e:
#                 message.info(request, "Your card has been declined.")
#         else:
#             result = transact({
#                 'amount': existing_order.get_cart_total(),
#                 'payment_method_nonce': request.POST['payment_method_nonce'],
#                 'options': {
#                     "submit_for_settlement": True
#                 }
#             })
#
#             if result.is_success or result.transaction:
#                 return redirect(reverse('shopping_cart:update_records',
#                         kwargs={
#                             'token': result.transaction.id
#                         })
#                     )
#             else:
#                 for x in result.errors.deep_errors:
#                     messages.info(request, x)
#                 return redirect(reverse('shopping_cart:checkout'))
#
#     context = {
#         'order': existing_order,
#         'client_token': client_token,
#         'STRIPE_PUBLISHABLE_KEY': publishKey
#     }
#
#     return render(request, 'shopping_cart/checkout.html', context)
#
#
# @login_required()
# def update_transaction_records(request, token):
#     # get the order being processed
#     order_to_purchase = get_user_pending_order(request)
#
#     # update the placed order
#     order_to_purchase.is_ordered=True
#     order_to_purchase.date_ordered=datetime.datetime.now()
#     order_to_purchase.save()
#
#     # get all items in the order - generates a queryset
#     order_items = order_to_purchase.items.all()
#
#     # update order items
#     order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())
#
#     # Add products to user profile
#     user_profile = get_object_or_404(Profile, user=request.user)
#     # get the products from the items
#     order_products = [item.product for item in order_items]
#     user_profile.ebooks.add(*order_products)
#     user_profile.save()
#
#
#     # create a transaction
#     transaction = Transaction(profile=request.user.profile,
#                             token=token,
#                             order_id=order_to_purchase.id,
#                             amount=order_to_purchase.get_cart_total(),
#                             success=True)
#     # save the transcation (otherwise doesn't exist)
#     transaction.save()
#
#
#     # send an email to the customer
#     # look at tutorial on how to send emails with sendgrid
#     messages.info(request, "Thank you! Your purchase was successful!")
# #     return redirect(reverse('accounts:my_profile'))
#
#
# def success(request, **kwargs):
#     # a view signifying the transcation was successful
#     return render(request, 'shopping_cart/purchase_success.html', {})

def register(request):

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

    #if not request.user.is_authenticated:

    if request.method == "GET":

        #return HttpResponseRedirect(reverse('login'))

        return render(request, "orders/login.html")



    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)






    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("orders:index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})



def logout_view(request):

    logout(request)

    return render(request, "orders/login.html", {"message": "Successfully logged out."})
