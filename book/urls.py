from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name = 'books'),
    path('sorted/', books_sorted_by_names, name='books_sorted_by_names'),
    path('sorted_desc/', books_sorted_by_names_desc, name='books_sorted_by_names_desc'),
    path('sorted_count/', books_sorted_by_count, name='books_sorted_by_count'),
    path('<int:bookid>/', book_by),
]