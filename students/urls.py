from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, LessonViewSet, HomeworkViewSet, register_user


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'homeworks', HomeworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
]