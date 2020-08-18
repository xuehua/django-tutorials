from django.urls import path
from . import views

urlpatterns = [
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<pk>/detail/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<pk>/add_author/', views.add_author, name='add_author'),
    path('author/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/<pk>/detail/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/<pk>/add_book/', views.add_book, name='add_book'),
]