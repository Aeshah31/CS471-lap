from django.urls import path
from . import views
from .views import simple_query, complex_query


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


    path('simple/query', simple_query, name='books_simple_query'),
    path('complex/query', complex_query, name='books_complex_query'),

    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task6', views.lab8_task5, name='lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='lab8_task7'),







]


