from rest_framework import serializers
# from django.contrib.auth.models import User
from app.models import *
from .order import OrderSerializer
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
 

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    # token = serializers.CharField(max_length=255, read_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    # def create(self, validated_data):
    #     # Use the `create_user` method we wrote earlier to create a new user.
    #     return UserModel.objects.create_user(**validated_data)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('is_superuser', 'is_active')





       