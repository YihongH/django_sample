from rest_framework import generics
# from django.contrib.auth.models import User
from ordertakeouts.models.location import Location
from ordertakeouts.models.order import Order
from ordertakeouts.models.user import User
from ordertakeouts.serializers.user import UserSerializer
from ordertakeouts.serializers.location import LocationSerializer
from ordertakeouts.serializers.order import OrderSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from datetime import datetime



class LocationList(generics.ListCreateAPIView):
    # serializer_class = LocationSerializer
    # def get_queryset(self):
    #     return Locations.objects.all()

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer