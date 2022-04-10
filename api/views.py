from .serializers import AuthorDetailSerializer
from .serializers import OrderDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserListSerializer, CreateUserSerializer, UserDetailSerializer
from author.models import Author
from order.models import Order

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


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializer


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Author.objects.all()


class RetrieveUpdateDestroyAuthorView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    serializer_class = AuthorDetailSerializer
    queryset = Author.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class RetrieveUpdateDestroyOrderrView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
