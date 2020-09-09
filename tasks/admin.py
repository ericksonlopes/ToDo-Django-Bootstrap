from django.contrib import admin

from tasks.models import TasksDB

@admin.register(TasksDB)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at']
