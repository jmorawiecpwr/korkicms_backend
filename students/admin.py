from django.contrib import admin
from .models import Lesson, Homework, Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'classtype', 'discord', 'classday', 'parent', 'hourly_rate', 'profile', 'additional_info']
    ordering = ['classtype', 'profile']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'topic', 'homework', 'is_settled', 'homework_done', 'homework_sent']

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['student', 'description']