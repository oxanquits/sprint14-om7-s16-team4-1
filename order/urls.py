from django.urls import path
from .views import *

urlpatterns = [
    path('', orders, name='orders'),
    path('add_order/', add_order, name='add_order'),
    path('<int:orderid>/', order_by),
    path('update_order/<str:orderid>/', update_order, name='update_order'),
]
