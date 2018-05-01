from rest_framework import viewsets
from ordertakeouts.models.model_locations import Locations
from ordertakeouts.models.model_orders import Orders
from ordertakeouts.models.model_users import Users
from .serializers.serializer_locations import LocationsSerializer
from .serializers.serializer_orders import OrdersSerializer
from .serializers.serializer_users import UsersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class LocationsViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Location instances.
    lookup_field = 'location_id'
    # permission_classes = (IsAuthenticated,)
    
    def list(self, request):

        queryset = Locations.Objects.all()
        serializer = LocationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, username=None):
        queryset = Locations.objects.all()
        location = get_object_or_404(quesryset, username=username)
        serializer = LocationsSerializer(location)
        return Response(serializer.data)

class OrdersViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer



class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = (IsAuthenticated,)