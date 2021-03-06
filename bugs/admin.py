from django.contrib import admin
from .models import Bug, BugComment


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'severity', 'status']
    list_filter = ['created']
    search_fields = ('title', 'description')


@admin.register(BugComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'bug', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('author', 'body')
