from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/deals
    path('', views.deals, name="deals-index"),
    path('1', views.twoforone, name="two-for-one")
]