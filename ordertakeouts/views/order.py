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




class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    # queryset=Orders.objects.all();
    # lookup_url_kwarg_id = "location_id"

    def get_queryset(self):
    # self: <ordertakeouts.views.orders.OrderList object at 0x107d308d0>
        # location_id = self.kwargs.get(self.lookup_url_kwarg_id)
        # orders = Orders.objects.filter(location=location_id)
        # created_time = self.request.GET.get('created_time')
    
        # import pdb; pdb.set_trace();                                                                                         
        created_time = self.request.query_params.get('created_time', None)
        # self.request: <rest_framework.request.Request object at 0x107d309e8>
        # self.request.query_params: <QueryDict: {'created_time': ['2018-05-07']}>
        # self.kwargs: {'location_id': '1'}
        # import pdb; pdb.set_trace()
        if created_time is not None:
            self.kwargs['created_time__contains'] = created_time
            # self.kwargs: {'location_id': '1', 'created_time__contains': '2018-05-07'}
            # self.kwargs['created_time__contains']=created_time;
        return Order.objects.filter(**self.kwargs);

    # def list(self, request, *args, **kwargs):
    #     # print("params")
    #     # print(request);
    #     # print("path variable")
    #     # print(kwargs);
    #     # location_id = kwargs["location_id"]
    #     # print(location_id);
    #     # get_queryset(self);
    #     created_time = request.GET.get('created_time');
    #     # import pdb; pdb.set_trace()
    #     if created_time is not None:
    #         kwargs['created_time__contains']=created_time;
    #         # kwargs['created_time__month']=time.month;
    #         # kwargs['created_time__day']=time.day;
    #     orders = self.get_queryset().filter(**kwargs);
                                                                  
    #     serializer = OrderSerializer(orders, many=True)
    #     # import pdb; pdb.set_trace()
    #     return Response(serializer.data)

    # lookup_url_kwarg_id = "location_id"
    def perform_create(self, serializer):
        import pdb; pdb.set_trace()
        # serializer.save(location_id=self.kwargs.get(self.lookup_url_kwarg_id))
        serializer.save(user=self.request.user, location_id=self.kwargs['location_id'])

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
