from rest_framework import generics
from app.models import *
from app.serializers import *
from guardian.shortcuts import assign_perm
from app.permissions import OrderPermission
from guardian.core import ObjectPermissionChecker
from drf_roles.mixins import RoleViewSetMixin
# from rolepermissions.mixins import HasRoleMixin
# from rolepermissions.mixins import HasPermissionsMixin

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from datetime import datetime


class OrderList(RoleViewSetMixin, generics.ListCreateAPIView):
    # import pdb; pdb.set_trace()
    permission_classes =  (OrderPermission, )
    serializer_class = OrderSerializer
   
    
    # queryset=Orders.objects.all();
    def get_queryset_for_admin(self):
        created_time = self.request.query_params.get('created_time', None)
        if created_time:
            self.kwargs['created_time__contains'] = created_time
        return Order.objects.filter(**self.kwargs)

    def get_queryset_for_delivery(self):
        created_time = self.request.query_params.get('created_time', None)
        if created_time:
            self.kwargs['created_time__contains'] = created_time
        return Order.objects.filter(**self.kwargs)

    def get_queryset_for_customer(self): 
        import pdb; pdb.set_trace()
        created_time = self.request.query_params.get('created_time', None)
        if created_time:
            self.kwargs['created_time__contains'] = created_time
        queryset = Order.objects.filter(**self.kwargs)
        checker = ObjectPermissionChecker(self.request.user) 
        checker.prefetch_perms(queryset)                                                               
        return [query for query in queryset if checker.has_perm('app.view_order', query)]
       
    # import pdb; pdb.set_trace()
    def perform_create(self, serializer):
        # import pdb; pdb.set_trace()   
        instance = serializer.save(user=self.request.user, location_id=self.kwargs['location_id'])
        assign_perm("app.change_order", self.request.user, instance)
        assign_perm("app.delete_order", self.request.user, instance)
        assign_perm("app.view_order", self.request.user, instance)
 

class OrderDetail(generics.RetrieveUpdateAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
