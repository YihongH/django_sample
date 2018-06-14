from app.models import User
from app.models import Order
from app.models import Location
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group


class CreateOrderTest(APITestCase):

    def setUp(self):    
        self.test_user = User.objects.create_user('test@example.com', 'testuser', 'testpassword')
        self.client.force_authenticate(self.test_user)
        self.test_user.groups.add(Group.objects.get(name='admin'))
        self.location = Location.objects.create(name='location_name',
                                                address='location_address')
        self.create_url = reverse('order-list', kwargs={'location_id': self.location.id})

    def test_create_order(self):
        data = {
            'comment' : 'test order'      
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comment'], data['comment'])

class ReadOrderTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('test@example.com','testuser', 'testpassword')
        self.client.force_authenticate(self.test_user)
        self.test_user.groups.add(Group.objects.get(name='admin'))
        self.location = Location.objects.create(name='location_name',
                                                address='location_address')
        self.order = Order.objects.create(location_id = self.location.id, comment='test order')
                                                
                                                 
    def test_read_order_list(self):
        response = self.client.get(reverse('order-list', kwargs={'location_id': self.location.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_order_detail(self):
        response = self.client.get(reverse('order-detail', args=[self.order.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)