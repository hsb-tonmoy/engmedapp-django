from django.urls import path
from .views import BoardList, ExplanationCreate, LevelList, PaperList, QuestionCreate, YearList, SessionList, QuestionList, SingleQuestion, SingleExplanation, CommentList

app_name = 'queestion_db'

urlpatterns = [
    path('list/', QuestionList.as_view(), name='question_list'),
    path('create/', QuestionCreate.as_view(), name='question_create'),
    path('boards/', BoardList.as_view(), name='boards_list'),
    path('levels/', LevelList.as_view(), name='levels_list'),
    path('papers/', PaperList.as_view(), name='papers_list'),
    path('years/', YearList.as_view(), name='years_list'),
    path('sessions/', SessionList.as_view(), name='sessions_list'),
    path('question/<slug:slug>/', SingleQuestion.as_view(), name='question'),
    path('explanation/create/', ExplanationCreate.as_view(), name='explanation'),
    path('explanation/<int:pk>/', SingleExplanation.as_view(), name='explanation'),
]
