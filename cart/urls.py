from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/cart
    path('cart', views.cart, name="cart"),
    path('add_to_cart', views.add_to_cart, name="add")
]