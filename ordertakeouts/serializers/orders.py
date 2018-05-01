from rest_framework import serializers, fields
from ordertakeouts.models.model_orders import Orders


class OrdersSerializer(serializers.ModelSerializer):

    location = serializers.StringRelatedField(many=False, read_only=True)
    user = serializers.StringRelatedField(many=False, read_only=True)
    # user_order = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = Orders
        fields = ('id', 'created_time', 'updated_time', 'comment', 'status', 'location', 'user', 'deleted')

    # def create(self, validated_data):
    #     orders_data = validated_data.pop('order_location')
    #     location = Locations.objects.create(**validated_data)
    #     for order_data in orders_data:
    #         Orders.objects.create(location=location, **order_data)
    #     return location

    # def update(self, instance, validated_data):
    #     orders_data = validated_data.pop('order_location')
    #     orders = (instance.order_location).all()
    #     orders = list(orders)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.save()

    #     for order_data in orders_data:
    #         order = orders.pop(0)
    #         order.comment = order_data.get('comment', order.comment)
    #         order.status = order_data.get('status', order.status)
    #         order.deleted = order_data.get('deleted', order.deleted)
    #         order.user = order_data.get('user', order.user)
    #         order.save()
    #     return instance  




	



       