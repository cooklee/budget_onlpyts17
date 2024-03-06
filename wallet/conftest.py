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