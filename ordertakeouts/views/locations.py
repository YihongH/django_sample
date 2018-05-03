from rest_framework import generics
# from django.contrib.auth.models import User
from ordertakeouts.models.locations import Locations
from ordertakeouts.models.orders import Orders
from ordertakeouts.models.users import Users
from ordertakeouts.serializers.users import UserSerializer
from ordertakeouts.serializers.locations import LocationSerializer
from ordertakeouts.serializers.orders import OrderSerializer
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from datetime import datetime



class LocationList(generics.ListCreateAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer