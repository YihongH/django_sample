from rest_framework import generics
# from django.contrib.auth.models import User
from .models.locations import Locations
from .models.orders import Orders
from .models.users import Users
from .serializers.users import UserSerializer
from .serializers.locations import LocationSerializer
from .serializers.orders import OrderSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# import pdb; pdb.set_trace()



# class LocationsViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing Location instances.
    # lookup_field = 'location_id'
    # permission_classes = (IsAuthenticated,)
    
    # def list(self, request):

    #     queryset = Locations.Objects.all()
    #     serializer = LocationsSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, username=None):
    #     queryset = Locations.objects.all()
    #     location = get_object_or_404(quesryset, username=username)
    #     serializer = LocationsSerializer(location)
    #     return Response(serializer.data)

# class OrdersViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)

#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializer
class LocationList(generics.ListCreateAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer



class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    lookup_url_kwarg_id = "location_id"


    def get_queryset(self):
        location_id = self.kwargs.get(self.lookup_url_kwarg_id)
        orders = Orders.objects.filter(location=location_id)
        created_time = self.request.GET.get('created_time')
        # created_time = param.get('created_time')
        # print(created_time);
        # print(type(created_time));
        # orders = Orders.objects.all();
        if created_time is not None:
            orders = Orders.objects.filter(location=location_id, created_time__year=created_time[:4],
                                                                 created_time__month=created_time[4:6],
                                                                 created_time__day=created_time[6:])                                                     
                                                            
        return orders

    def perform_create(self, serializer):
        serializer.save(location_id=self.kwargs.get(self.lookup_url_kwarg_id))

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class UserList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

