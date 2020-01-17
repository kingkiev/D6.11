from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, authors_create_many, books_authors_create_many, FriendList, FriendFormEdit, books_friends_create, index

app_name = 'p_library'  
urlpatterns = [  
	path('', index, name='index'), 
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', authors_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('friend/create', FriendFormEdit.as_view(), name='friend_create'),
    path('friends', FriendList.as_view(), name='friend_form'),
    path('book_friend/create', books_friends_create, name='book_friend_create'),
    ] 