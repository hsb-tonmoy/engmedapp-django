from rest_framework import serializers
from accounts.models import Accounts
from .models import Board, Level, Paper, Year, Session, Question, Explanation, Comment

from drf_writable_nested.serializers import WritableNestedModelSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('user_name',)


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = "__all__"


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class CommentListSerializer(serializers.ModelSerializer):
    author = AccountSerializer(required=False, many=False, read_only=False)

    class Meta:
        model = Comment
        fields = "__all__"


class ExplanationListSerializer(serializers.ModelSerializer):
    author = AccountSerializer(required=False, many=False, read_only=False)
    comments = CommentListSerializer(many=True, read_only=False)

    class Meta:
        model = Explanation
        fields = ('question', 'excerpt', 'author',
                  'published', 'status', 'comments')


class QuestionListSerializer(serializers.ModelSerializer):

    board = BoardSerializer(many=False, read_only=False)
    level = LevelSerializer(many=False, read_only=False)
    paper = PaperSerializer(many=False, read_only=False)
    year = YearSerializer(many=False, read_only=False)
    session = SessionSerializer(many=False, read_only=False)

    class Meta:
        model = Question
        fields = ('board', 'level', 'paper', 'year', 'session', 'title',
                  'excerpt', 'published', 'slug')


class SingleQuestionSerializer(WritableNestedModelSerializer):

    board = BoardSerializer(many=False, read_only=False)
    level = LevelSerializer(many=False, read_only=False)
    paper = PaperSerializer(many=False, read_only=False)
    year = YearSerializer(many=False, read_only=False)
    session = SessionSerializer(many=False, read_only=False)
    explanations = ExplanationListSerializer(many=True, read_only=False)
    author = AccountSerializer(required=False, many=False, read_only=False)

    class Meta:
        model = Question
        fields = "__all__"
        lookup_field = 'slug'


class SingleExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"
