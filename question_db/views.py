from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from vote.views import VoteMixin
from django_filters import rest_framework as filters
from .models import Board, Level, Paper, Year, Session, Question, Explanation, Comment
from .serializers import BoardSerializer, ExplanationCreateSerializer, LevelSerializer, PaperSerializer, QuestionCreateSerializer, QuestionUpdateSerializer, YearSerializer, SessionSerializer, QuestionListSerializer, SingleQuestionSerializer, ExplanationSerializer, ExplanationCreateSerializer, CommentListSerializer
from .permissions import ExplanationPermissions


class Board(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class Level(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class Paper(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class Year(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class Session(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class QuestionPagination(PageNumberPagination):
    page_size = 1

    def get_paginated_response(self, data):
        response = super(QuestionPagination, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.filter(status='published')
    serializer_class = QuestionListSerializer
    pagination_class = QuestionPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
        'board__name': ["in", "exact"],
        'level__name': ["in", "exact"],
        'paper__name': ["in", "exact"],
        'year__name': ["in", "exact"],
        'session__name': ["in", "exact"],
        'author__username': ["in", "exact"],
    }
    permission_classes = [IsAuthenticatedOrReadOnly]


class QuestionCreate(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer
    permission_classes = [DjangoModelPermissions]


class SingleQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = SingleQuestionSerializer
    lookup_field = 'slug'


class SingleQuestionUpdate(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionUpdateSerializer
    lookup_field = 'slug'


class Explanation(viewsets.ModelViewSet, VoteMixin):
    permission_classes = [ExplanationPermissions,
                          DjangoModelPermissionsOrAnonReadOnly]
    queryset = Explanation.objects.all()
    serializer_class = ExplanationSerializer

    def create(self, request):
        serializer = ExplanationCreateSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(status="published")
    serializer_class = CommentListSerializer
