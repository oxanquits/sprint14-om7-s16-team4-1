from django.contrib.auth import get_user_model
from rest_framework import serializers
from book.models import Book

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('last_login', )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('last_login', 'password')


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'authors')


class BookDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
