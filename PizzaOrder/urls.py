from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/PizzaLair
    path('', views.order, name="order-index"),
    path('<int:id>', views.get_pizza_by_id, name="pizza_details"),
]