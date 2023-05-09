from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/cart
    path('', views.cart_detail, name="cart"),
    path('add-to-cart/<int:item_id>', views.add_to_cart, name='add_to_cart'),
]