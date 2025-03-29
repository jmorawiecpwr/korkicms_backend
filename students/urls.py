from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, LessonViewSet, HomeworkViewSet


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'homeworks', HomeworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]