from django.urls import path

from . import views
#list of urls supported by this app (orders)
urlpatterns = [
    path("", views.index, name="index")
]
