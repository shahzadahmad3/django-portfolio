from django.contrib import admin
from .models import Post, Author, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    search_fields = ('title', 'body')
    list_filter = ('published_at', 'categories')
    date_hierarchy = 'published_at'
    ordering = ('-published_at',)
    filter_horizontal = ('categories',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

