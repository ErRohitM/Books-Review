from django.urls import path
from . views import index,add_book,search_books,showbook,write_review,show_review

urlpatterns = [
    path('', index, name='index'),
    path('addbook/', add_book, name='add_book'),
    path('search_books/', search_books, name='search_books'),
    path('search_books/<str:pk>', showbook, name='showbooks'),
    path('search_books/review/<str:pk>', write_review, name='write-review'),
     path('search_books/show_review/<str:pk>', show_review, name='show_review'),
    ]
