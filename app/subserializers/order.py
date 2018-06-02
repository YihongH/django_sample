from rest_framework import serializers
from app.models import Order


class OrderSerializer(serializers.ModelSerializer):

    location = serializers.StringRelatedField(many=False, read_only=True)
    user = serializers.StringRelatedField(many=False, read_only=True)
    # user_order = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'created_time', 'updated_time', 'comment', 'status', 'location', 'user', 'deleted')

  
    
    


	



       