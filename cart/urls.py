from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/cart
    path('', views.cart_detail, name="cart"),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('add-deal-to-cart/<int:pizza_id>/<int:pizza1_id>', views.add_deal_to_cart, name='add_deal_to_cart'),
    path('add-pofmonth_to-cart/<int:id>', views.add_pofmonth_to_cart, name='add_pofmonth_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove-deal/<int:cart_item_id>/', views.remove_deal_from_cart, name='remove_deal_from_cart'),
    path('checkout', views.checkout, name="checkout"),
    path('payment', views.payment, name="payment")
]