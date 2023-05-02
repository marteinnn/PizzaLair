from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/menu
    path('', views.frontpage, name="frontpage-index"),
]