from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Lesson, Homework
from .serializers import StudentSerializer, LessonSerializer, HomeworkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Użytkownik utworzony"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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