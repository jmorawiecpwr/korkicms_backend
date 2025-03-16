from rest_framework import serializers
from .models import Student, LessonTopic, Homework

class LessonTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTopic
        fields = '__all__'

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    topics = LessonTopicSerializer(many=True, read_only=True)
    homeworks = HomeworkSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'