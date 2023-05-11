from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/cart
    path('', views.cart_detail, name="cart"),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('add-deal-to-cart/<str:typeofdeal>/<int:pizza_id>/<int:pizza1_id>', views.add_deal_to_cart, name='add_deal_to_cart'),
    path('add-pofmonth_to-cart/<int:id>', views.add_pofmonth_to_cart, name='add_pofmonth_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove-deal/<str:typeofdeal>/<int:cart_item_id>/', views.remove_deal_from_cart, name='remove_deal_from_cart'),
    path('checkout', views.checkout, name="checkout"),
    path('clear-cart', views.clear_cart, name="clear_cart"),
    path('decrease-quantity/<int:cart_item_id>', views.decrease_quantity, name='decrease_quantity'),
    path('increase-quantity/<int:cart_item_id>', views.increase_quantity, name='increase_quantity'),
    path('decrease-deal-quantity/<str:typeofdeal>/<int:item_id>', views.decrease_deal_quantity, name='decrease_deal_quantity'),
    path('increase-deal-quantity/<str:typeofdeal>/<int:item_id>', views.increase_deal_quantity, name='increase_deal_quantity'),
    path('payment', views.payment, name="payment"),
    path('reviews', views.review, name="review"),
    path('pick-payment', views.pickpayment, name="pick-payment"),
    path('confirmation', views.confirmation, name="confirmation")
]