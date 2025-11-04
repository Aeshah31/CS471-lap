from django.contrib import admin
from .models import Book, Booklap
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_year", "created_at")
    search_fields = ("title", "author")
    list_filter = ("published_year",)



@admin.register(Booklap)
class BooklapAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price', 'edition')
    fields = ('title', 'author', 'price', 'edition')

from .models import Student, Address

admin.site.register(Student)
admin.site.register(Address)
