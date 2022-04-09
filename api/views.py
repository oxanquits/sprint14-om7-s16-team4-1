from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserListSerializer, CreateUserSerializer, UserDetailSerializer

User = get_user_model()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
