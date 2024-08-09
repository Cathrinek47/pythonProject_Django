from django.contrib import admin
from task_manager.models import *

# admin.site.register(Task, TaskAdmin)
# admin.site.register(SubTask, SubTaskAdmin)
# admin.site.register(Category, CategoryAdmin)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline','create_at')
    search_fields = ('title',)
    list_filter = ('status', 'categories')
    ordering = ('-create_at',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'deadline', 'create_at')
    search_fields = ('title', 'task__title')
    list_filter = ('status', 'task')
    ordering = ('-create_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

