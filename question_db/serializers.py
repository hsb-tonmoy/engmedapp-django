from rest_framework import serializers
from accounts.models import Accounts
from .models import Board, Level, Paper, Year, Session, Question, Explanation, Comment

from drf_writable_nested.serializers import WritableNestedModelSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('id', 'user_name')


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
    author = AccountSerializer(many=False, read_only=False)

    class Meta:
        model = Question
        fields = ('id', 'board', 'level', 'paper', 'year', 'session', 'title',
                  'excerpt', 'published', 'slug', 'author', 'status')

    # def create(self, validated_data):
    #     boards = validated_data.pop('board', [])
    #     levels = validated_data.pop('level', [])
    #     papers = validated_data.pop('paper', [])
    #     years = validated_data.pop('year', [])
    #     sessions = validated_data.pop('session', [])

    #     author = validated_data.pop('author')

    #     instance = Question.objects.create(**validated_data)

    #     for board_data in boards:
    #         board = Board.objects.get(pk=board_data.get('id'))
    #         instance.board.add(board)

    #     for level_data in levels:
    #         level = Level.objects.get(pk=level_data.get('id'))
    #         instance.level.add(level)

    #     for paper_data in papers:
    #         paper = Paper.objects.get(pk=paper_data.get('id'))
    #         instance.paper.add(paper)

    #     for year_data in years:
    #         year = Board.objects.get(pk=year_data.get('id'))
    #         instance.year.add(year)

    #     for session_data in sessions:
    #         session = Session.objects.get(pk=session_data.get('id'))
    #         instance.session.add(session)

    #     author = Accounts.objects.get(pk=author_data.get('user_name'))

    #     instance.author.add(author)

    #     return instance

    # def update(self, instance, validated_data):

    #     boards = validated_data.pop('board', [])
    #     levels = validated_data.pop('level', [])
    #     papers = validated_data.pop('paper', [])
    #     years = validated_data.pop('year', [])
    #     sessions = validated_data.pop('session', [])

    #     author_data = validated_data.pop('author')

    #     instance = super().update(instance, validated_data)

    #     for board_data in boards:
    #         board = Board.objects.get(pk=board_data.get('id'))
    #         instance.board.add(board)

    #     for level_data in levels:
    #         level = Level.objects.get(pk=level_data.get('id'))
    #         instance.level.add(level)

    #     for paper_data in papers:
    #         paper = Paper.objects.get(pk=paper_data.get('id'))
    #         instance.paper.add(paper)

    #     for year_data in years:
    #         year = Board.objects.get(pk=year_data.get('id'))
    #         instance.year.add(year)

    #     for session_data in sessions:
    #         session = Session.objects.get(pk=session_data.get('id'))
    #         instance.session.add(session)

    #     author = Accounts.objects.get(pk=author_data.get('user_name'))

    #     instance.author.add(author)

    #     return instance


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


class QuestionCreateSerializer(serializers.ModelSerializer):

    board = serializers.PrimaryKeyRelatedField(
        queryset=Board.objects.all(), many=False)
    level = serializers.PrimaryKeyRelatedField(
        queryset=Level.objects.all(), many=False)
    paper = serializers.PrimaryKeyRelatedField(
        queryset=Paper.objects.all(), many=False)
    year = serializers.PrimaryKeyRelatedField(
        queryset=Year.objects.all(), many=False)
    session = serializers.PrimaryKeyRelatedField(
        queryset=Session.objects.all(), many=False)
    author = serializers.PrimaryKeyRelatedField(
        queryset=Accounts.objects.all(), many=False)

    class Meta:
        model = Question
        fields = ("title", "excerpt", "content", "verified_explanation", "status", "board", "level",
                  "paper", "year", "session", "author", "slug", "published")


class ExplanationCreateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = ("question", "excerpt", "content", "author", "status")


class SingleExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"
