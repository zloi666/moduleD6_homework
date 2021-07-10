from django.contrib import admin
from django.urls import path
from .views import AuthorEdit, AuthorList, authors_create_many, FriendList, FriendEdit, FriendBookList

app_name = 'library'

urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('author/create_many', authors_create_many, name='author_create_many'),
    path('friends/', FriendList.as_view(), name='friend_list'),
    path('friends/create', FriendEdit.as_view(), name='friend_create'),
    path('friend_books/', FriendBookList.as_view(), name='friend_books_list'),
]
