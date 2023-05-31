from django.contrib import admin

from tasks.models import Tasks, Type


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass
