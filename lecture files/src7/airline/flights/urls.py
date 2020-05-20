from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resister", views.register, name="register"),
    path("login", views.login_view, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]
