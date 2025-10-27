from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links_view, name='links'),
    path('html5/text', views.formatting_view, name='formatting'),
    path('html5/listing', views.listing_view, name='listing'),
    path('html5/tabels', views.tabels_view, name='tabels'),
    path('search/', views.search_view, name='search'),



]
