from rest_framework import generics
from app.models import Location
from app.serializers import LocationSerializer
from app.permissions import CustomModelPermissions
# from datetime import datetime



class LocationList(generics.ListCreateAPIView):
    # serializer_class = LocationSerializer
    # def get_queryset(self):
    #     return Locations.objects.all()
    permission_classes =  (CustomModelPermissions, )
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =  (CustomModelPermissions, )
    queryset = Location.objects.all()
    serializer_class = LocationSerializer