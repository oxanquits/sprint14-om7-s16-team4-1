from django.urls import path
from . import views

retrieve_update_delete_methods = {
    'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
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
    path('order/<int:id>/', views.RetrieveUpdateDestroyOrderView.as_view()),

    path(
        'books/', views.BookViewSet.as_view({'get': 'list'}), name='book_list_api'),
    path('create_book/',
         views.BookViewSet.as_view({'post': 'create'}), name='create_book_api'),
    path('book/<int:id>/', views.BookViewSet.as_view(retrieve_update_delete_methods),
         name='retrieve_book_api'),

    path('user/<int:user_id>/orders/', views.UserOrderViewSet.as_view({'get': 'list'}), name='user_order_list_api'),
    path('user/<int:user_id>/create_order/', views.UserOrderViewSet.as_view({'post': 'create'}),
         name='create_user_order_api'),
    path('user/<int:user_id>/order/<int:order_id>/', views.UserOrderViewSet.as_view(retrieve_update_delete_methods),
         name='user_order_detail_api'),
]
