from django.db import models

# Create your models here.
class Deals(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    image = models.CharField(max_length=999)

    def __str__(self):
        return self.name