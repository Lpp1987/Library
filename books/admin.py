from django.contrib import admin

# Register your models here.
from books.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ['last_name', 'first_name']
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ['title', 'author']
    pass
