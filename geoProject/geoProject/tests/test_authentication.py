from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
def test_jwt_authentication_works():
    user_credentials = {
        'username': 'testuser',
        'password': 'testpassword'
    }

    User.objects.create_user(**user_credentials)

    # Log in and obtain a JWT token
    client = APIClient()
    login_url = '/api/token/'
    response = client.post(login_url, data=user_credentials)

    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
