from django.contrib import admin
from .models import *

admin.site.register(Notes)


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['user', 'subjects', 'title', 'description', 'due', 'is_finished']


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_finished']
