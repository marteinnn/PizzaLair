from django.db import models
from django.contrib.auth.models import User
from menu.models import Pizza
from deals.models import Deals
import uuid

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    product = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='items')
    deals = models.ForeignKey(Deals, on_delete=models.CASCADE, related_name='deals')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
