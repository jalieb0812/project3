from django.urls import path

from . import views
#list of urls supported by this app (orders)
urlpatterns = [
    path("", views.index, name="index"),
    #path("register", views.register, name="register"),
    #path("login", views.login_view, name="index"),
    #path("logout", views.logout_view, name="logout"),
]
