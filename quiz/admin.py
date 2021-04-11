from django.contrib import admin
from .models import Categories, Quizzes, Question, Answer

# Register your models here.


@admin.register(Categories)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'date_created',
        'date_updated',
        'get_categories'
    ]


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_correct'
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
        'date_updated'
    ]
    inlines = [
        AnswerInlineModel,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_correct',
        'question'
    ]
