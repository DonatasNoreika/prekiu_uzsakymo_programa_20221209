from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField("Pavadinimas", max_length=200)
    price = models.FloatField("Kaina")

class Status(models.Model):
    name = models.CharField("Pavadinimas", max_length=200)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField("Data", auto_now_add=True)
    status = models.ForeignKey("Status", on_delete=models.SET_NULL, null=True, blank=True)

class OrderLine(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True, blank=True)
    qty = models.IntegerField("Kiekis")
