from app.models import User
from app.models import Location
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


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

class ReadLocationTest(APITestCase):
    
    def setUp(self):
        self.test_superuser = User.objects.create_superuser('supertest@example.com','supertestuser', 'supertestpassword')
        self.client.force_authenticate(self.test_superuser)
        self.location = Location.objects.create(name='location_name',
                                                address='location_address')

    def test_read_location_list(self):
        response = self.client.get(reverse('location-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_location_detail(self):
        response = self.client.get(reverse('location-detail', args=[self.location.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)