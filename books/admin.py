from django.contrib import admin

from books.models import Author, Book, User


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ['last_name', 'first_name']
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ['title', 'author']
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ordering = ['-is_staff']
    pass
