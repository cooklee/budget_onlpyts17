from django.contrib.auth.models import User
from django.db import models

TYPES = (
        (1, 'income'),
        (2, 'expanse')
    )
# Create your models here.

class Wallet(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)
class CashFlow(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    category = models.ManyToManyField(Category)
    date = models.DateField()
    type = models.IntegerField(choices=TYPES)