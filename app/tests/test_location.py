from app.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.views import UserList

from app.serializers import UserSerializer


class CreateLocationTest(APITestCase):

    def setUp(self):    
        self.test_superuser = User.objects.create_superuser('supertest@example.com', 'supertestuser', 'supertestpassword')
        self.client.force_authenticate(self.test_superuser)
        self.create_url = reverse('location-list')

    def test_create_location(self):
        data = {
            'name': 'location_name',
            'address': 'location_address'       
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['address'], data['address'])