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

    def __str__(self):
        return f"{self.name} stan: {self.balance}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CashFlow(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    category = models.ManyToManyField(Category, blank=True)
    date = models.DateField()
    type = models.IntegerField(choices=TYPES)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        if self.type == 1:
            self.wallet.balance += self.amount
        elif self.type == 2:
            self.wallet.balance -= self.amount
        self.wallet.save()
