from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionView, Board, Level, Paper,  Session, TagView, Year, ExplanationView

app_name = 'question_db'

router = DefaultRouter()
router.register(r'questions', QuestionView)
router.register(r'explanations', ExplanationView)
router.register(r'board', Board)
router.register(r'level', Level)
router.register(r'paper', Paper)
router.register(r'year', Year)
router.register(r'session', Session)

urlpatterns = [
    path('tags/', TagView.as_view(), name='tags_list'),
    path('', include(router.urls)),
]
