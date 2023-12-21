from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from geoWorld.models import Municipality


class MunicipalityViewSetTest(APITestCase):
    def setUp(self):
        # Create a user and obtain a token
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = str(RefreshToken.for_user(self.user).access_token)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.municipality_data = {
            "name": "Test Municipality",
            "geometry": "MULTIPOLYGON (((0 0, 0 1, 1 1, 1 0, 0 0)))",
        }
        self.municipality = Municipality.objects.create(**self.municipality_data)
        self.url = reverse("municipality-list")

    def test_list_municipalities(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_municipality(self):
        new_municipality_data = {
            "name": "New Municipality",
            "geometry": "MULTIPOLYGON (((2 2, 2 3, 3 3, 3 2, 2 2)))",
        }
        response = self.client.post(self.url, new_municipality_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Municipality.objects.count(), 2)

    def test_retrieve_municipality(self):
        detail_url = reverse("municipality-detail", args=[self.municipality.id])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.municipality_data["name"])

    def test_update_municipality(self):
        update_data = {
            "name": "Updated Municipality",
            "geometry": "MULTIPOLYGON (((1 1, 1 2, 2 2, 2 1, 1 1)))",
        }
        detail_url = reverse("municipality-detail", args=[self.municipality.id])
        response = self.client.put(detail_url, update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.municipality.refresh_from_db()
        self.assertEqual(self.municipality.name, update_data["name"])

    def test_delete_municipality(self):
        detail_url = reverse("municipality-detail", args=[self.municipality.id])
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Municipality.objects.count(), 0)
