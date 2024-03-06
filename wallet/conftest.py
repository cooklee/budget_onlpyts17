import pytest
from django.contrib.auth.models import User

from wallet.models import Wallet

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
def wallets(user, user2):
    wallets = []
    wallets2 = []
    for x in range(5):
        wallet = Wallet.objects.create(name=x, owner=user)
        wallet2 = Wallet.objects.create(name=x, owner=user2)
        wallets.append(wallet)
        wallets2.append(wallet2)
    return wallets, wallets2

