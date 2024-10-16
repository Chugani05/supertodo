from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
