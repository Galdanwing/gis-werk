from urllib.parse import urlencode

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from geoWorld.models import Municipality


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def authenticated_api_client(api_client):
    user = User.objects.create_user(username="testuser", password="testpassword")
    token = str(RefreshToken.for_user(user).access_token)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


@pytest.fixture
def municipality_data():
    return {
        "name": "Test Municipality",
        "geometry": "MULTIPOLYGON (((0 0, 0 1, 1 1, 1 0, 0 0)))",
    }


@pytest.fixture
@pytest.mark.django_db
def create_municipality(authenticated_api_client, municipality_data):
    url = reverse("municipality-list")
    response = authenticated_api_client.post(url, municipality_data, format="json")
    return response


@pytest.mark.django_db
def test_list_municipalities(authenticated_api_client, create_municipality):
    url = reverse("municipality-list")
    response = authenticated_api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_list_municipalities_in_bbox_filter(authenticated_api_client, create_municipality):
    url = reverse("municipality-list")
    other_municipality_data = {
        "name": "Other Municipality",
        "geometry": "MULTIPOLYGON (((7 54, 7 55, 8 55, 8 54, 7 54)))",
    }
    Municipality.objects.create(**other_municipality_data)

    bbox_filter_params = {"in_bbox": "0,0,1,1"}
    response = authenticated_api_client.get(f"{url}?{urlencode(bbox_filter_params)}")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == "Test Municipality"


@pytest.mark.django_db
def test_create_municipality(authenticated_api_client, municipality_data):
    url = reverse("municipality-list")
    response = authenticated_api_client.post(url, municipality_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Municipality.objects.count() == 1


@pytest.mark.django_db
def test_retrieve_municipality(authenticated_api_client, create_municipality):
    municipality_id = create_municipality.data["id"]
    detail_url = reverse("municipality-detail", args=[municipality_id])
    response = authenticated_api_client.get(detail_url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "Test Municipality"


@pytest.mark.django_db
def test_update_municipality(authenticated_api_client, create_municipality):
    municipality_id = create_municipality.data["id"]
    update_data = {
        "name": "Updated Municipality",
        "geometry": "MULTIPOLYGON (((1 1, 1 2, 2 2, 2 1, 1 1)))",
    }
    detail_url = reverse("municipality-detail", args=[municipality_id])
    response = authenticated_api_client.put(detail_url, update_data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert Municipality.objects.get(id=municipality_id).name == "Updated Municipality"


@pytest.mark.django_db
def test_delete_municipality(authenticated_api_client, create_municipality):
    municipality_id = create_municipality.data["id"]
    detail_url = reverse("municipality-detail", args=[municipality_id])
    response = authenticated_api_client.delete(detail_url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Municipality.objects.count() == 0
