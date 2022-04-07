from django.urls import path
from .views import *

urlpatterns = [
    path('', users, name='users'),
    path('add_user/', add_user, name='add_user'),
]
