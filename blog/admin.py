from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created')
    list_filter = ('created', 'author')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
