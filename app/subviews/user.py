from rest_framework import generics
# from django.contrib.auth.models import User
from app.models import *
from app.serializers import *

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