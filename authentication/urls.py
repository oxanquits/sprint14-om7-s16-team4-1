from django.urls import path
from .views import *

urlpatterns = [
    path('', users, name='users'),
    path('add_user/', add_user, name='add_user'),
    path('users/', users, name='users'),
    path('delete_user/<str:userid>/', delete_user, name='delete_user'),
]
