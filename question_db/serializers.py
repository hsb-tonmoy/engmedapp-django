from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Accounts
from .models import Board, Level, Paper, Year, Session, Question, Explanation, Comment
from taggit.models import Tag
from drf_writable_nested.serializers import WritableNestedModelSerializer
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class AccountSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(source="profile.profile_pic")
    city = serializers.CharField(source="profile.city")
    country = serializers.CharField(source="profile.country")
    phone_no = serializers.CharField(source="profile.phone_no")
    name_of_institution = serializers.CharField(
        source="profile.name_of_institution")

    class Meta:
        model = Accounts
        fields = ('id', 'email', 'username',
                  'first_name', 'last_name', 'account_type', 'is_verified', 'profile_pic', 'name_of_institution', 'city', 'country', 'phone_no')


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
        fields = ('id', 'question', 'author', 'content',
                  'published', 'status', 'comments')


class QuestionListSerializer(TaggitSerializer, serializers.ModelSerializer):

    board = BoardSerializer(many=False, read_only=False)
    level = LevelSerializer(many=False, read_only=False)
    paper = PaperSerializer(many=False, read_only=False)
    year = YearSerializer(many=False, read_only=False)
    session = SessionSerializer(many=False, read_only=False)
    author = AccountSerializer(many=False, read_only=False)
    tags = TagListSerializerField()

    is_bookmarked = serializers.SerializerMethodField(
        method_name='get_is_bookmarked')

    def get_is_bookmarked(self, obj):
        request = self.context.get('request')
        if request:
            user = request.user
            if user.is_authenticated:
                return obj.bookmark_check(user)
        return False

    class Meta:
        model = Question
        fields = ('id', 'board', 'level', 'paper', 'year', 'session', 'title',
                  'excerpt', 'tags', 'published', 'slug', 'author', 'published', 'status', 'is_bookmarked')


class SingleQuestionSerializer(TaggitSerializer, WritableNestedModelSerializer):

    board = BoardSerializer(many=False, read_only=False)
    level = LevelSerializer(many=False, read_only=False)
    paper = PaperSerializer(many=False, read_only=False)
    year = YearSerializer(many=False, read_only=False)
    session = SessionSerializer(many=False, read_only=False)
    explanations = ExplanationListSerializer(many=True, read_only=False)
    author = AccountSerializer(required=False, many=False, read_only=False)
    tags = TagListSerializerField()

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


class QuestionUpdateSerializer(serializers.ModelSerializer):

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
                  "paper", "year", "session", "author", "slug")


class ExplanationCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Explanation
        fields = ("question", "content", "author")

    def save(self, **kwargs):

        kwargs["author"] = self.fields["author"].get_default()
        return super().save(**kwargs)


class ExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"


class TagSerializer(TaggitSerializer, serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"
