from django.contrib import admin

from wallet.models import Category, CashFlow, Wallet

# Register your models here.
admin.site.register(Category)
admin.site.register(CashFlow)
admin.site.register(Wallet)