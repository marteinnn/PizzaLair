from django.urls import path
from . import views
urlpatterns = [
    #http://localhost:8000/PizzaLair
    path('', views.landingPage, name="landingPage"),
]