from order.models import Order
from author.models import Author
from book.models import Book
from . import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import OrderDetailSerializer
from .serializers import AuthorDetailSerializer

User = get_user_model()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.CreateUserSerializer


class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = serializers.AuthorDetailSerializer


class AuthorListView(generics.ListAPIView):
    serializer_class = serializers.AuthorDetailSerializer
    queryset = Author.objects.all()


class RetrieveUpdateDestroyAuthorView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    serializer_class = serializers.AuthorDetailSerializer
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


class BookViewSet(ModelViewSet):
    lookup_url_kwarg = 'id'
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BookListSerializer

        return serializers.BookDetailedSerializer
