from rest_framework import generics
# from django.contrib.auth.models import User
from app.models import *
from app.serializers import *

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import viewsets

from rest_framework import status
# from django.contrib.auth import login, authenticate
from rest_framework.views import APIView


class UserList(generics.ListAPIView):
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

  
# class IsStaffOrTargetUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # allow user to list all users if logged in user is staff
#         return view.action == 'retrieve' or request.user.is_staff

#     def has_object_permission(self, request, view, obj):
#         # allow logged in user to view own details, allows staff to view all records
#         return request.user.is_staff or obj == request.user


# class UserView(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     model = get_user_model()
#     queryset = User.objects.all()

#     def get_permissions(self):
#         # allow non-authenticated user to create via POST
#         return (permissions.AllowAny() if self.request.method == 'POST'
#                 else IsStaffOrTargetUser()),
