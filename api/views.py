from django.contrib.auth import get_user_model
from rest_framework import generics

from rest_framework.viewsets import ModelViewSet
from . import serializers
from book.models import Book

from author.models import Author

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


class BookViewSet(ModelViewSet):
    lookup_url_kwarg = 'id'
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BookListSerializer

        return serializers.BookDetailedSerializer
