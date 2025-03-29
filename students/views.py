from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Lesson, Homework
from .serializers import StudentSerializer, LessonSerializer, HomeworkSerializer
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.none()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.none()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lesson.objects.filter(student__owner=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data['student'].owner != self.request.user:
            raise PermissionDenied("Nie możesz dodawać lekcji do tego ucznia.")
        serializer.save()


    def get_queryset(self):
        return Lesson.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.none()
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Homework.objects.filter(student__owner=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data['student'].owner != self.request.user:
            raise PermissionDenied("Nie możesz dodawać pracy domowej do tego ucznia.")
        serializer.save()