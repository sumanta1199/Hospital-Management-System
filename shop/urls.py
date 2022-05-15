from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index),
    path("tracker", views.tracker),
    path("search", views.search),
    path("products/<int:myid>", views.productView),
    path("checkout", views.checkout),


]
