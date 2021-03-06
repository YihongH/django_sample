from app.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CreateUserTest(APITestCase):
    
    def test_create_user(self):
        url = reverse('user-create')
        data = {
            'username': 'createuser',
            'email': 'createuser@example.com',
            'password': 'somepassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

class ReadUserTest(APITestCase):
    def setUp(self):
        self.test_superuser = User.objects.create_superuser('supertest@example.com','supertestuser', 'supertestpassword')
        self.client.force_authenticate(self.test_superuser)
        self.user = User.objects.create(username='readuser',
                                        email='readuser@example.com',
                                        password='somepassword')
 
    def test_read_user_list(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
