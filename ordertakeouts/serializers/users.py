from rest_framework import serializers, fields
# from django.contrib.auth.models import User
from ordertakeouts.models.users import Users
from ordertakeouts.models.orders import Orders

from .orders import OrderSerializer


class UserSerializer(serializers.ModelSerializer):
    
    order_user = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'created_time', 'updated_time', 'order_user')
        
    # def create(self, validated_data):
    #     orders_data = validated_data.pop('order_user')
    #     user = Users.objects.create(**validated_data)
    #     for order_data in orders_data:
    #         Orders.objects.create(user=user, **order_data)
    #     return user

    # def update(self, instance, validated_data):
    #     orders_data = validated_data.pop('order_user')
    #     orders = (instance.order_location).all()
    #     orders = list(orders)
    #     instance.first_name= validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.save()

    #     for order_data in orders_data:
    #         order = orders.pop(0)
    #         order.comment = order_data.get('comment', order.comment)
    #         order.status = order_data.get('status', order.status)
    #         order.deleted = order_data.get('deleted', order.deleted)
    #         order.location = order_data.get('location', order.location)
    #         order.save()
    #     return instance  




	



       