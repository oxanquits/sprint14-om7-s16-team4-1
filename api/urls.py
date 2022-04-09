from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user_list_api'),
    path('create_user/', views.CreateUserView.as_view(), name='create_user_api'),
    path('user/<int:id>/', views.RetrieveUpdateDestroyUserView.as_view(),
         name='user_detail_api'),
    path('authors/', views.AuthorListView.as_view()),
    path('create_author/', views.AuthorCreateView.as_view()),
    path('author/<int:id>/', views.RetrieveUpdateDestroyAuthorView.as_view()),

]
