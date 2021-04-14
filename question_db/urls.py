from django.urls import path
from .views import BoardList, LevelList, PaperList, YearList, SessionList, QuestionList, SingleQuestion, ExplanationList, SingleExplanation, CommentList

app_name = 'queestion_db'

urlpatterns = [
    path('list/', QuestionList.as_view(), name='question_list'),
    path('boards/', BoardList.as_view(), name='boards_list'),
    path('levels/', LevelList.as_view(), name='levels_list'),
    path('papers/', PaperList.as_view(), name='papers_list'),
    path('years/', YearList.as_view(), name='years_list'),
    path('sessions/', SessionList.as_view(), name='sessions_list'),
    path('question/<slug:slug>/', SingleQuestion.as_view(), name='question'),
    # path('explanations/', ExplanationList.as_view(), name='explanations'),
    path('explanation/<int:pk>/', SingleExplanation.as_view(), name='explanation'),
]
