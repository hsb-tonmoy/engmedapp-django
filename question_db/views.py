from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import filters as f
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from vote.views import VoteMixin
from django_filters import rest_framework as filters
from taggit.models import Tag

from .filters import QuestionFilterSet
from .models import Board, Level, Paper, Year, Session, Question, Explanation, Comment
from .serializers import BoardSerializer, ExplanationCreateSerializer, LevelSerializer, PaperSerializer, QuestionCreateSerializer, QuestionUpdateSerializer, YearSerializer, SessionSerializer, QuestionListSerializer, SingleQuestionSerializer, ExplanationSerializer, ExplanationCreateSerializer, CommentListSerializer, TagSerializer
from .permissions import ExplanationPermissions

User = get_user_model()


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
    page_size = 10

    def get_paginated_response(self, data):
        response = super(QuestionPagination, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = QuestionListSerializer
    pagination_class = QuestionPagination
    filter_backends = (filters.DjangoFilterBackend, f.OrderingFilter,)
    filterset_class = QuestionFilterSet
    lookup_field = 'slug'

    retrieve_serializer_class = SingleQuestionSerializer
    create_serializer_class = QuestionCreateSerializer
    update_serializer_class = QuestionUpdateSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'retrieve_serializer_class'):
                return self.retrieve_serializer_class

        elif self.action == 'create':
            if hasattr(self, 'create_serializer_class'):
                return self.create_serializer_class

        elif self.action == 'update':
            if hasattr(self, 'update_serializer_class'):
                return self.update_serializer_class

        return super(QuestionView, self).get_serializer_class()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if request.query_params:
            if request.query_params.get('bookmark'):
                user = User.objects.get(
                    username=request.query_params.get('bookmark'))
                question_ids = [flag.object_id for flag in Question.get_flags_for_types(
                    [Question], user=user, status=1)[Question]]
                queryset = Question.objects.filter(id__in=question_ids)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.query_params:
            if request.query_params.get('bookmark') == '1':
                instance.bookmark_add(user=request.user)

            elif request.query_params.get('bookmark') == '0':
                instance.bookmark_remove(request.user)

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ExplanationView(viewsets.ModelViewSet, VoteMixin):
    permission_classes = [ExplanationPermissions,
                          DjangoModelPermissionsOrAnonReadOnly]
    queryset = Explanation.objects.all()
    serializer_class = ExplanationSerializer

    create_serializer_class = ExplanationCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            if hasattr(self, 'create_serializer_class'):
                return self.create_serializer_class

        return super(ExplanationView, self).get_serializer_class()


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(status="published")
    serializer_class = CommentListSerializer


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (f.SearchFilter,)
    search_fields = ('name',)
