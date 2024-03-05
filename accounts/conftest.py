import pytest
from django.contrib.auth.models import User


@pytest.fixture
def uzytkownik():
    return User.objects.create_user(username='test', password='testowe')