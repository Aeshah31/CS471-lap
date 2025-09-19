from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.order_by("-created_at")
    return render(request, "bookmodule/book_list.html", {"books": books})
