import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


# Create your tests here.

def test_create_user_get():
    client = Client()
    url = reverse('create_user')
    response = client.get(url)
    assert response.status_code == 200


def test_create_user_post_diff_password():
    client = Client()
    url = reverse('create_user')
    data = {'username': 'u', 'password': 'abc', 'password2': 'cba'}
    response = client.post(url, data)
    assert response.status_code == 200
    assert response.context['error'] == 'hasła są różne'

@pytest.mark.django_db
def test_create_user_post():
    client = Client()
    url = reverse('create_user')
    data = {'username': 'u', 'password': 'abc', 'password2': 'abc'}
    response = client.post(url, data)
    assert response.status_code == 302
    user = User.objects.get(username='u')


@pytest.mark.django_db
def test_login_post(uzytkownik):
    pass
