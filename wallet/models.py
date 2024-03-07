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
    amount = models.FloatField(default=0)#100  -> 150
    category = models.ManyToManyField(Category, blank=True)
    date = models.DateField()
    type = models.IntegerField(choices=TYPES)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            old_amount=0
        else:
            old_cf = CashFlow.objects.get(pk=self.pk)
            old_amount = old_cf.amount
        super().save(force_insert, force_update, using, update_fields)
        if self.type == 1:
            self.wallet.balance += self.amount - old_amount
        elif self.type == 2:
            self.wallet.balance -= self.amount - old_amount


        self.wallet.save()
