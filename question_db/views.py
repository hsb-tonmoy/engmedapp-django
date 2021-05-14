from django_filters import rest_framework as filters
from rest_framework import generics, viewsets
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from vote.views import VoteMixin
from .models import Board, Level, Paper, Year, Session, Question, Explanation, Comment
from .serializers import BoardSerializer, ExplanationCreateSerializer, LevelSerializer, PaperSerializer, QuestionCreateSerializer, QuestionUpdateSerializer, YearSerializer, SessionSerializer, QuestionListSerializer, SingleQuestionSerializer, ExplanationSerializer, ExplanationCreateSerializer, CommentListSerializer
from .permissions import ExplanationPermissions


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SingleBoard(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class LevelList(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SingleLevel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class PaperList(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SinglePaper(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class YearList(generics.ListCreateAPIView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SingleYear(generics.RetrieveUpdateDestroyAPIView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SingleSession(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class QuestionsFilter(filters.FilterSet):

    class Meta:
        model = Question
        fields = ('board__name', 'level__name',
                  'paper__name', 'year__name', 'session__name')


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.filter(status='published')
    serializer_class = QuestionListSerializer
    filterset_class = QuestionsFilter
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
