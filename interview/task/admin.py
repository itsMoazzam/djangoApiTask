from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner', 'status', 'created_at')
    search_fields = ('title', 'owner__email', 'status')
    list_filter = ('status', 'created_at')

admin.site.register(Task, TaskAdmin)