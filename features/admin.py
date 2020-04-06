from django.contrib import admin
from .models import Feature, FeatureComment


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']
    list_filter = ['created']
    search_fields = ('title', 'description')


@admin.register(FeatureComment)
class FeatureCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'feature', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('author', 'body')
