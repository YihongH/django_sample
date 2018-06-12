from app.models import User
from app.models import Order
from app.models import Location
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CreateOrderTest(APITestCase):

    def setUp(self):    
        self.test_superuser = User.objects.create_superuser('supertest@example.com', 'supertestuser', 'supertestpassword')
        self.client.force_authenticate(self.test_superuser)
        self.location = Location.objects.create(name='location_name',
                                                address='location_address')
        self.create_url = reverse('order-list', args=[self.location.id])

    def test_create_order(self):
        data = {
            'comment' : 'test order'      
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comment'], data['comment'])

class ReadOrderTest(APITestCase):
    def setUp(self):
        self.test_superuser = User.objects.create_superuser('supertest@example.com','supertestuser', 'supertestpassword')
        self.client.force_authenticate(self.test_superuser)
        self.location = Location.objects.create(name='location_name',
                                                address='location_address')
        self.order = Order.objects.create(location_id = self.location.id, comment='test order')
                                                
                                                 
    def test_read_order_list(self):
        response = self.client.get(reverse('order-list', kwargs={'location_id': self.location.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_order_detail(self):
        response = self.client.get(reverse('order-detail', args=[self.order.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)