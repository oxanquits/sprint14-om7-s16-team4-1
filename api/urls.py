from django.urls import path
from . import views

book_api_methods = {
    'get': 'retrieve', 'post': 'create',
    'put': 'update', 'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user_list_api'),
    path('create_user/', views.CreateUserView.as_view(), name='create_user_api'),
    path('user/<int:id>/', views.RetrieveUpdateDestroyUserView.as_view(), name='user_detail_api'),

    path('books/', views.BookViewSet.as_view({'get': 'list'}), name='book_list_api'),
    path('book/<int:id>/', views.BookViewSet.as_view(book_api_methods), name='retrieve_book_api'),
]
