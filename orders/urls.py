from django.urls import path

from django.conf.urls import url

from . import views,
(
    add_to_cart,
    #delete_from_cart,
    order_details,
    #checkout,
    #update_transaction_records,
    #success
)

#list of urls supported by this app (orders)
urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),


    # item_id sent over by object_id from index
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),


    url(r'^order-summary/$', order_details, name="order_summary"),
    #url(r'^success/$', success, name='purchase_success'),
    #url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    #url(r'^checkout/$', checkout, name='checkout'),
    #url(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records,
        #name='update_records')

]
