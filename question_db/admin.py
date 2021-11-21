from django.contrib import admin
from .models import Board, Level, Paper, Year, Session, Question, Explanation, Comment

# Register your models here.

admin.site.register(Comment)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name')
    fieldsets = (
        (None, {'fields': ('name',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title',)}
         ),
    )


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name')
    fieldsets = (
        (None, {'fields': ('name',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title',)}
         ),
    )


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name')
    fieldsets = (
        (None, {'fields': ('name',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title',)}
         ),
    )


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name')
    fieldsets = (
        (None, {'fields': ('name',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title',)}
         ),
    )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name')
    fieldsets = (
        (None, {'fields': ('name',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title',)}
         ),
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_filter = ('status', 'board', 'level', 'paper', 'year', 'session')
    ordering = ('-published',)
    list_display = ('title', 'author', 'slug', 'board',
                    'level', 'paper', 'year', 'session', 'status')
    fieldsets = (
        (None, {'fields': ('title', 'board', 'level', 'paper',
         'year', 'session', 'excerpt', 'content', 'verified_explanation', 'tags', 'status')}),
        (None, {'fields': ('published', 'author')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'board', 'level', 'paper', 'year', 'session', 'excerpt', 'content', 'verified_explanation', 'tags' 'status', 'author', 'published')}
         ),
    )


@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
    search_fields = ('question', 'content')
    list_filter = ('status', 'author')
    ordering = ('-published',)
    list_display = ('id', '__str__', 'author', 'published', 'status')
    fieldsets = (
        (None, {'fields': ('question', 'content',)}),
        (None, {'fields': ('published', 'author', 'status')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('question', 'content', 'published', 'author', 'status')}
         ),
    )
