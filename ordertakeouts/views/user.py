from rest_framework import generics
# from django.contrib.auth.models import User
from ordertakeouts.models.location import Location
from ordertakeouts.models.order import Order
from ordertakeouts.models.user import User
from ordertakeouts.serializers.user import UserSerializer
from ordertakeouts.serializers.location import LocationSerializer
from ordertakeouts.serializers.order import OrderSerializer
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework import permissions



class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer


def update_users(request, user_id):
    user = User.objects.get(pk=user_id)
    user.users.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()