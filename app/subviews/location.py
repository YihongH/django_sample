from rest_framework import generics
# from django.contrib.auth.models import User
from app.models import *
from app.serializers import *

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