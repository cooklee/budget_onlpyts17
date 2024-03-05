import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_empty():
    pass

def test_base_view():
    url = reverse('home')
    client = Client()
    response = client.get(url)
    assert response.status_code == 200


