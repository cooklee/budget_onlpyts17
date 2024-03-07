from datetime import datetime

import pytest
from django.test import Client
from django.urls import reverse

from wallet.forms import WalletCreateForm
from wallet.models import Wallet, CashFlow


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


@pytest.mark.django_db()
def test_cashflow_save_income(wallet):
    cf = CashFlow(wallet=wallet, amount=100, date=datetime.now(), type=1)
    cf.save()
    wallet.refresh_from_db()
    assert wallet.balance == 100

@pytest.mark.django_db()
def test_cashflow_create_expanse_cf_created(wallet, cashflow):
    cf = CashFlow(wallet=wallet, amount=50, date=datetime.now(), type=2)
    cf.save()
    wallet.refresh_from_db()
    assert wallet.balance == 50

@pytest.mark.django_db()
def test_cashflow_update_income_smaller(wallet, cashflow):
    cashflow.amount = 50
    cashflow.save()
    wallet.refresh_from_db()
    assert wallet.balance == 50

@pytest.mark.django_db()
def test_cashflow_update_income_bigger(wallet, cashflow):
    cashflow.amount = 150
    cashflow.save()
    wallet.refresh_from_db()
    assert wallet.balance == 150

@pytest.mark.django_db()
def test_cashflow_update_expanse_bigger(wallet, cashflow_expanse):
    cashflow_expanse.amount = 75
    cashflow_expanse.save()
    wallet.refresh_from_db()
    assert wallet.balance == 25

@pytest.mark.django_db()
def test_cashflow_update_expanse_smaller(wallet, cashflow_expanse):
    cashflow_expanse.amount = 25
    cashflow_expanse.save()
    wallet.refresh_from_db()
    assert wallet.balance == 75
