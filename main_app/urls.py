from django.urls import path
from . import views


urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('authors/', views.AuthorList.as_view(), name="author_list"),
  path('authors/new/', views.AuthorCreate.as_view(), name="author_create"),
  path('authors/<int:pk>/', views.AuthorDetail.as_view(), name="author_detail"),
  path('authors/<int:pk>/update',views.AuthorUpdate.as_view(), name="author_update"),
  path('authors/<int:pk>/delete',views.AuthorDelete.as_view(), name="author_delete"),
  path('authors/<int:pk>/books/new/', views.BookCreate.as_view(), name="book_create"),
  path('books/', views.BookList.as_view(), name="book_list"),
  path('books/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
  path('books/<int:pk>/update',views.BookUpdate.as_view(), name="book_update"),
  path('books/<int:pk>/delete',views.BookDelete.as_view(), name="book_delete"),
  path('readinglists/<int:pk>/books/<int:book_pk>/', views.ReadinglistBookAssoc.as_view(), name="readinglist_book_assoc"),      
]