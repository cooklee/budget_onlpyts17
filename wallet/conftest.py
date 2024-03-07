from datetime import datetime

import pytest
from django.contrib.auth.models import User

from wallet.models import Wallet, CashFlow


@pytest.fixture
def user():
    return User.objects.create_user(username='test', password='test')

@pytest.fixture
def user2():
    return User.objects.create_user(username='test2', password='test')

@pytest.fixture
def wallet(user):
    return Wallet.objects.create(name='test', owner=user)


@pytest.fixture
def cashflow(wallet):
    cf = CashFlow(wallet=wallet, amount=100, date=datetime.now(), type=1)
    cf.save()
    return cf

@pytest.fixture
def cashflow_expanse(cashflow, wallet):
    cf = CashFlow(wallet=wallet, amount=50, date=datetime.now(), type=2)
    cf.save()
    return cf

@pytest.fixture
def wallets(user, user2):
    wallets = []
    wallets2 = []
    for x in range(5):
        wallet = Wallet.objects.create(name=x, owner=user)
        wallet2 = Wallet.objects.create(name=x, owner=user2)
        wallets.append(wallet)
        wallets2.append(wallet2)
    return wallets, wallets2

