from rest_framework import serializers
from .models import Student, Homework, Lesson

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['owner']

class StudentSerializer(serializers.ModelSerializer):
    topics = LessonSerializer(many=True, read_only=True)
    homeworks = HomeworkSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        exclude = ['owner']