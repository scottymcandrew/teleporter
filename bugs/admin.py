from django.contrib import admin
from .models import Bug


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
    list_filter = ['created']
