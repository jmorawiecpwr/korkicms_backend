from django.contrib import admin
from .models import LessonTopic, Homework, Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'classtype', 'discord', 'classday', 'parent', 'hourly_rate', 'profile', 'additional_info']
    ordering = ['classtype', 'profile']

@admin.register(LessonTopic)
class LessonTopicAdmin(admin.ModelAdmin):
    list_display = ['student', 'title']

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['student', 'description']