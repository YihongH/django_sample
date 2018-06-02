from rest_framework import generics
from app.models import Order
from app.serializers import OrderSerializer
from guardian.shortcuts import assign_perm
from app.permissions import CustomObjectPermissions
from app.permissions import OrderPermissions
from guardian.core import ObjectPermissionChecker
# from drf_roles.mixins import RoleViewSetMixin
from app.mixins import RoleViewSetMixin
# from datetime import datetime


class OrderList(RoleViewSetMixin, generics.ListCreateAPIView):

    permission_classes =  (OrderPermissions, )
    serializer_class = OrderSerializer
   
    # import pdb; pdb.set_trace()
    queryset=Order.objects.none();
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
        created_time = self.request.query_params.get('created_time', None)
        if created_time:
            self.kwargs['created_time__contains'] = created_time
        queryset = Order.objects.filter(**self.kwargs)
        checker = ObjectPermissionChecker(self.request.user) 
        checker.prefetch_perms(queryset)                                                               
        return [query for query in queryset if checker.has_perm('app.view_order', query)]
    
    
    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user, location_id=self.kwargs['location_id'])
        assign_perm("app.change_order", self.request.user, instance)
        assign_perm("app.delete_order", self.request.user, instance)
        assign_perm("app.view_order", self.request.user, instance)


class OrderDetail(generics.RetrieveUpdateAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
