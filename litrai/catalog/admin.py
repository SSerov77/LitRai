from django.contrib import admin
from .models import Category, Author, Book

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publish_date', 'book_type', 'price', 'is_available')
    list_filter = ('category', 'author', 'book_type', 'is_available', 'publish_date')
    search_fields = ('title', 'author__name', 'category__name')
    list_editable = ('price', 'is_available')

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'category', 'description', 'cover_image')
        }),
        ('Availability', {
            'fields': ('price', 'book_type', 'publish_date', 'is_available'),
        }),
    )