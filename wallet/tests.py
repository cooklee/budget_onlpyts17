import pytest
from django.test import Client
from django.urls import reverse

from wallet.forms import WalletCreateForm
from wallet.models import Wallet


@pytest.mark.django_db
def test_empty():
    pass


def test_base_view():
    url = reverse('home')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


def test_create_wallet_view_not_logged():
    client = Client()
    url = reverse('add_wallet')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_create_wallet_view_get(user):
    client = Client()
    client.force_login(user)
    url = reverse('add_wallet')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], WalletCreateForm)


@pytest.mark.django_db
def test_create_wallet_view_post(user):
    client = Client()
    client.force_login(user)
    url = reverse('add_wallet')
    data = {'name': 'Some Name'}
    response = client.post(url, data)
    assert response.status_code == 302
    assert Wallet.objects.get(name='Some Name')


@pytest.mark.django_db
def test_get_wallet_delete(wallet):
    client = Client()
    client.force_login(wallet.owner)
    url = reverse('delete_wallet', kwargs={'pk': wallet.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['wallet'] == wallet


@pytest.mark.django_db
def test_post_wallet_delete(wallet):
    client = Client()
    client.force_login(wallet.owner)
    url = reverse('delete_wallet', kwargs={'pk': wallet.pk})
    data = {
        'delete': 'tak'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    with pytest.raises(Wallet.DoesNotExist):
        Wallet.objects.get(pk=wallet.pk)

@pytest.mark.django_db
def test_post_wallet_delete(wallet, user2):
    client = Client()
    client.force_login(user2)
    url = reverse('delete_wallet', kwargs={'pk': wallet.pk})
    data = {
        'delete': 'tak'
    }
    response = client.post(url, data)
    assert response.status_code == 403
    assert Wallet.objects.get(pk=wallet.pk)


@pytest.mark.django_db
def test_list_wallets(wallets, user):
    client = Client()
    client.force_login(user)
    url = reverse('list_wallet')
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context['wallets']) == wallets[0]

