from django.contrib import admin
from .models import Task, Project, TaskPhoto


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'project',
                    'creation_date', 'due_date', 'priority', 'is_complete')
    list_filter = ('creation_date', 'due_date', 'priority', 'is_complete')
    search_fields = ('title', 'description')
    list_editable = ('priority', 'is_complete')
    list_per_page = 20
    ordering = ('priority',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    list_per_page = 20
    ordering = ('created_at',)


admin.site.register(TaskPhoto)
