from django.urls import path
from .views import *

urlpatterns = [
    path('', orders, name='orders'),
    path('add_order/', add_order, name='add_order'),
]
