from rest_framework import generics
from app.models import *
from app.serializers import *

# from app.permissions import LocationPermission

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