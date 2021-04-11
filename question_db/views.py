from django.shortcuts import render
from django_filters import rest_framework as filters
from django_filters.fields import CSVWidget
from rest_framework import generics
from .models import Board, Level, Paper, Year, Session, Question, Explanation, Comment
from .serializers import BoardSerializer, LevelSerializer, PaperSerializer, YearSerializer, SessionSerializer, QuestionListSerializer, SingleQuestionSerializer, ExplanationListSerializer, SingleExplanationSerializer, CommentListSerializer


class BoardList(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class LevelList(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class PaperList(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class YearList(generics.ListCreateAPIView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class QuestionsFilter(filters.FilterSet):

    class Meta:
        model = Question
        fields = ('board__name', 'level__name',
                  'paper__name', 'year__name', 'session__name')


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.filter(status='published')
    serializer_class = QuestionListSerializer
    filterset_class = QuestionsFilter
    # filterset_fields = ('board__name', 'level__name',
    #                     'paper__name', 'year__name', 'session__name')


class SingleQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = SingleQuestionSerializer
    lookup_field = 'slug'


class ExplanationList(generics.ListCreateAPIView):
    queryset = Explanation.objects.filter(status="published")
    serializer_class = ExplanationListSerializer


class SingleExplanation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Explanation.objects.all()
    serializer_class = SingleExplanationSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(status="published")
    serializer_class = CommentListSerializer

# class CommentUpdateDelete(generics.RetrieveUpdateDestroyAPIVieww):
#     queryset = Comment.objects.all()
