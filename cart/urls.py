from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/cart
    path('', views.cart_detail, name="cart"),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout', views.checkout, name="checkout"),
]