from django.urls import path
from .views import *

urlpatterns = [
    path('', authors, name = 'authors'),
    path('<int:authorid>/', author_books),
    path('add_author/', add_author, name='add_author'),
]