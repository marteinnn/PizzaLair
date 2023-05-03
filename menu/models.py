from django.db import models

# Create your models here.
class Topping(models.Model):
    TID = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)

class Pizza(models.Model):
    PID = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=9999)
    description = models.CharField(max_length=9999)
    spicy = models.BooleanField()
    vegan = models.BooleanField()

class PizzaToppings(models.Model):
    PID = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    TID = models.ForeignKey(Topping, on_delete=models.CASCADE)

