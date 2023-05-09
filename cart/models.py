from django.db import models
from django.contrib.auth.models import User
from menu.models import Pizza
from deals.models import Deals
import uuid

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, default=None)
    deal = models.ForeignKey(Deals, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.product.name
