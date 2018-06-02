from rest_framework import generics
from app.models import User
from app.serializers import UserSerializer

from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import viewsets

from rest_framework.views import APIView
from app.permissions import CustomModelPermissions


class UserList(generics.ListAPIView):
    permission_classes =  (CustomModelPermissions, )
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):

    model = get_user_model()
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer

  
