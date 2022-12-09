from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField("Pavadinimas", max_length=200)
    price = models.FloatField("Kaina")

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField("Pavadinimas", max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField("Data", auto_now_add=True)
    status = models.ForeignKey("Status", on_delete=models.SET_NULL, null=True, blank=True)

    def bendra_suma(self):
        total = 0
        lines = self.lines.all()
        for line in lines:
            total += line.product.price * line.qty
        return total

    def __str__(self):
        return f"{self.date} ({self.status})"

class OrderLine(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True, blank=True)
    qty = models.IntegerField("Kiekis")

    def suma(self):
        return self.product.price * self.qty