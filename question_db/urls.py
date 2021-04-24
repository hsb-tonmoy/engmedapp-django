from django.urls import path
from .views import BoardList, ExplanationCreate, LevelList, PaperList, QuestionCreate, SingleBoard, SingleLevel, SinglePaper, SingleQuestionUpdate, SingleSession, SingleYear, YearList, SessionList, QuestionList, SingleQuestion, SingleExplanation, CommentList

app_name = 'queestion_db'

urlpatterns = [
    path('list/', QuestionList.as_view(), name='question_list'),
    path('create/', QuestionCreate.as_view(), name='question_create'),
    path('update/<slug:slug>/', SingleQuestionUpdate.as_view(),
         name='question_create'),
    path('boards/', BoardList.as_view(), name='boards_list'),
    path('board/<int:pk>/', SingleBoard.as_view(), name='board'),
    path('levels/', LevelList.as_view(), name='levels_list'),
    path('level/<int:pk>/', SingleLevel.as_view(), name='level'),
    path('papers/', PaperList.as_view(), name='papers_list'),
    path('paper/<int:pk>/', SinglePaper.as_view(), name='paper'),
    path('years/', YearList.as_view(), name='years_list'),
    path('year/<int:pk>/', SingleYear.as_view(), name='year'),
    path('sessions/', SessionList.as_view(), name='sessions_list'),
    path('session/<int:pk>/', SingleSession.as_view(), name='session'),
    path('question/<slug:slug>/', SingleQuestion.as_view(), name='question'),
    path('explanation/create/', ExplanationCreate.as_view(), name='explanation'),
    path('explanation/<int:pk>/', SingleExplanation.as_view(), name='explanation'),
]
