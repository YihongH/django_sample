from rest_framework import serializers
from app.models import Location
from app.models import Order
from .order import OrderSerializer


class LocationSerializer(serializers.ModelSerializer):
    
    order_location = OrderSerializer(many=True, read_only=True)
    
    class Meta:
        model = Location
        fields = ('id', 'name', 'address', 'created_time', 'updated_time', 'order_location')



