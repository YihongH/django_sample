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




class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    # check queryset
    # queryset=Orders.objects.all();
    # lookup_url_kwarg_id = "location_id"


    def get_queryset(self):
        # location_id = self.kwargs.get(self.lookup_url_kwarg_id)
        # orders = Orders.objects.filter(location=location_id)
        # created_time = self.request.GET.get('created_time')
        # # created_time = param.get('created_time')
        # # print(created_time);
        # # print(type(created_time));
        # queryset = Orders.objects.all();
        # if created_time is not None:
        #     orders = Orders.objects.filter(location=location_id, created_time__year=created_time[:4],
        #                                                          created_time__month=created_time[4:6],
        #      
        # import pdb; pdb.set_trace();                                                                                         
        created_time = self.request.query_params.get('created_time', None)
        # created_time = self.kwargs['created_time'];
        # import pdb; pdb.set_trace()
        if created_time is not None:
            self.kwargs['created_time__contains'] = created_time
        #     self.kwargs['created_time__contains']=created_time;
            # kwargs['created_time__month']=time.month;
        #     # kwargs['created_time__day']=time.day;
        # orders = self.get_queryset().filter(**kwargs);
        # f(created_time=time,**kwargs)
        return Orders.objects.filter(**self.kwargs);

    # def list(self, request, *args, **kwargs):
    #     # print("params")
    #     # print (request);
    #     # print("path variable")
    #     # print (kwargs);
    #     # location_id = kwargs["location_id"]
    #     # print (location_id);
    #     # get_queryset(self);
    #     created_time = request.GET.get('created_time');
    #     # import pdb; pdb.set_trace()
    #     if created_time is not None:
    #         kwargs['created_time__contains']=created_time;
    #         # kwargs['created_time__month']=time.month;
    #         # kwargs['created_time__day']=time.day;
    #     orders = self.get_queryset().filter(**kwargs);
    #     # f(created_time=time,**kwargs);

                                                   
                      
    #     serializer = OrderSerializer(orders, many=True)
    #     # import pdb; pdb.set_trace()
    #     return Response(serializer.data)

    # lookup_url_kwarg_id = "location_id"
    def perform_create(self, serializer):
        # serializer.save(location_id=self.kwargs.get(self.lookup_url_kwarg_id))
        serializer.save(location_id=self.kwargs['location_id'])

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
