from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Board, Level, Paper, Session, Year, QuestionCreate, SingleQuestionUpdate, QuestionList, SingleQuestion, Explanation

app_name = 'question_db'

router = DefaultRouter()
router.register(r'explanations', Explanation)
router.register(r'board', Board)
router.register(r'level', Level)
router.register(r'paper', Paper)
router.register(r'year', Year)
router.register(r'session', Session)

urlpatterns = [
    path('list/', QuestionList.as_view(), name='question_list'),
    path('create/', QuestionCreate.as_view(), name='question_create'),
    path('update/<slug:slug>/', SingleQuestionUpdate.as_view(),
         name='question_create'),
    path('question/<slug:slug>/', SingleQuestion.as_view(), name='question'),
    path('', include(router.urls)),
]
