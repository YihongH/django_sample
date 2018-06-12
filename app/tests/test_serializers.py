from app.models import User
from app.models import Location
from app.serializers import LocationSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SerializerLocationTest(APITestCase):

    def setUp(self):
        self.location_attributes = {'name': 'location_name', 'address': 'location_address'}
        self.location = Location.objects.create(**self.location_attributes)
        self.serializer = LocationSerializer(instance=self.location)


    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'address', 'created_time', 'updated_time', 'order_location']))