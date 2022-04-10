from django.urls import path
from . import views

book_api_methods = {
    'get': 'retrieve', 'put': 'update',
    'patch': 'partial_update', 'delete': 'destroy'
}

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user_list_api'),
    path('create_user/', views.CreateUserView.as_view(), name='create_user_api'),
    path('user/<int:id>/', views.RetrieveUpdateDestroyUserView.as_view(),
         name='user_detail_api'),

    path('authors/', views.AuthorListView.as_view()),
    path('create_author/', views.AuthorCreateView.as_view()),
    path('author/<int:id>/', views.RetrieveUpdateDestroyAuthorView.as_view()),

    path('orders/', views.OrderListView.as_view()),
    path('create_order/', views.OrderCreateView.as_view()),
    path('order/<int:id>/', views.RetrieveUpdateDestroyOrderrView.as_view()),

    path(
        'books/', views.BookViewSet.as_view({'get': 'list'}), name='book_list_api'),
    path('create_book/',
         views.BookViewSet.as_view({'post': 'create'}), name='create_book_api'),
    path('book/<int:id>/', views.BookViewSet.as_view(book_api_methods),
         name='retrieve_book_api'),
]
