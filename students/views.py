from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, LessonTopic, Homework
from .serializers import StudentSerializer, LessonTopicSerializer, HomeworkSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LessonTopicViewSet(viewsets.ModelViewSet):
    queryset = LessonTopic.objects.all()
    serializer_class = LessonTopicSerializer

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer