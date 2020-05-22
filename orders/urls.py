from django.urls import path, re_path

from django.conf.urls import url

from . import views


app_name = 'orders'
#list of urls supported by this app (orders)
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),


    # item_id sent over by object_id from index
    #path('cart/add/<int:item_id>', views.add_item, name='add_item'),
    path('add-to-cart/<int:ordered_item_id>', views.add_to_cart, name="add_to_cart"),

    path(r'^order-summary/$', views.order_details, name="order_summary"),
    path(r'^success/$', views.success, name='purchase_success'),
    path(r'^item/delete/(?P<item_id>[-\w]+)/$', views.delete_from_cart, name='delete_item'),
    path(r'^checkout/$', views.checkout, name='checkout'),
    #below payment route not implented
    path(r'^payment/(?P<order_id> [-\w]+)/$', views.process_payment, name='process_payment' ),
    path(r'^update-transaction/(?P<order_id>[-\w]+)/$', views.update_transaction_records,
        name='update_records') # redirects to the update

    #probably change url to path in this paths
]
