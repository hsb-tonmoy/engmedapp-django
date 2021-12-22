from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TeacherView

app_name = 'teacher_db'
router = DefaultRouter()
router.register(r'teachers', TeacherView)

urlpatterns = [
    path('', include(router.urls)),
]
