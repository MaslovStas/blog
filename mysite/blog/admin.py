from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    search_fields = ['title', 'body']
    list_filter = ['status', 'publish', 'created', 'author']
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ['author']
    ordering = ['-status', 'publish']
    date_hierarchy = 'publish'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
