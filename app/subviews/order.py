from rest_framework import generics
from app.models import *
from app.serializers import *
# from rolepermissions.mixins import HasRoleMixin
# from rolepermissions.mixins import HasPermissionsMixin

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from datetime import datetime




class OrderList(generics.ListCreateAPIView):

    serializer_class = OrderSerializer
    # queryset=Orders.objects.all();

    def get_queryset(self):
    # self: <app.views.orders.OrderList object at 0x107d308d0>
    
        # import pdb; pdb.set_trace();                                                                                         
        created_time = self.request.query_params.get('created_time', None)
        # self.request: <rest_framework.request.Request object at 0x107d309e8>
        # self.request.query_params: <QueryDict: {'created_time': ['2018-05-07']}>
        # self.kwargs: {'location_id': '1'}
        # import pdb; pdb.set_trace()
        if created_time:
            self.kwargs['created_time__contains'] = created_time
            # self.kwargs: {'location_id': '1', 'created_time__contains': '2018-05-07'}
        return Order.objects.filter(**self.kwargs);

    # import pdb; pdb.set_trace()
    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()
        # serializer.save(location_id=self.kwargs.get(self.lookup_url_kwarg_id))    
        serializer.save(user=self.request.user, location_id=self.kwargs['location_id'])
   

class OrderDetail(generics.RetrieveUpdateAPIView):
  
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
