from django.contrib import admin
from .models import Feature, FeatureComment


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'severity', 'status']
    list_filter = ['created']


@admin.register(FeatureComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'bug', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('author', 'body')