from django.db import models
from django.contrib.auth.models import User
from menu.models import Pizza
from deals.models import Deals
import uuid

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.pizza.name

class CartItemDeals(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, default=None, related_name="firstpizza")
    pizza1 = models.ForeignKey(Pizza, on_delete=models.CASCADE, default=None, related_name="secondpizza")
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.name

