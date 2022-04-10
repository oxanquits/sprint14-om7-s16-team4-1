from rest_framework.response import Response
from rest_framework import status
from order.models import Order
from author.models import Author
from book.models import Book
from . import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import OrderDetailSerializer
from django.shortcuts import get_object_or_404

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


class RetrieveUpdateDestroyOrderView(generics.RetrieveUpdateDestroyAPIView):
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


class UserOrderViewSet(GenericViewSet):
    serializer_class = OrderDetailSerializer

    def list(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        orders = self.get_serializer_class()(user.order_set, many=True).data
        return Response(orders)

    def retrieve(self, request, user_id, order_id):
        user, order = get_user_and_order(user_id, order_id)
        return Response(self.get_serializer_class()(order).data)

    def create(self, request, user_id):
        data = request.data
        data.update({'user': user_id})
        order = self.get_serializer_class()(data=data)
        if order.is_valid(raise_exception=True):
            order.save()
            return Response(order.data, status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, user_id, order_id):
        user, order = get_user_and_order(user_id, order_id)
        serializer = self.get_serializer_class()(instance=order, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response({"detail": "Bad request."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, user_id, order_id):
        user, order = get_user_and_order(user_id, order_id)
        order.delete()
        return Response({"detail": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


def get_user_and_order(user_id, order_id):
    user = get_object_or_404(User, id=user_id)
    order = user.order_set.filter(id=order_id).first()
    if order is None:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    return user, order
