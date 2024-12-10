from datetime import datetime
from dis import Positions

from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    # t = models.TextChoices()

class Seller(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    data = models.DateTimeField()

class Item(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()

class Order(models.Model):
    date = models.DateTimeField(default=datetime.now())
    total = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order_positions(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

