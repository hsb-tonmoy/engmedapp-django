from django.db import models
from vote.models import VoteModel
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from autoslug import AutoSlugField
from accounts.models import Accounts
from taggit.managers import TaggableManager
from siteflags.models import ModelWithFlag

from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.search import SearchVector

from django.db.models.signals import post_save
from django.dispatch import receiver


class Board(models.Model):
    class Meta:

        verbose_name = _("Board")
        verbose_name_plural = _("Boards")
        ordering = ["id"]

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Level(models.Model):
    class Meta:

        verbose_name = _("Level")
        verbose_name_plural = _("Levels")
        ordering = ["name"]

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Paper(models.Model):
    class Meta:

        verbose_name = _("Paper")
        verbose_name_plural = _("Papers")
        ordering = ["name"]

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Year(models.Model):
    class Meta:

        verbose_name = _("Year")
        verbose_name_plural = _("Years")
        ordering = ["name"]

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Session(models.Model):
    class Meta:

        verbose_name = _("Session")
        verbose_name_plural = _("Sessions")
        ordering = ["name"]

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(ModelWithFlag):

    board = models.ForeignKey(Board, on_delete=models.DO_NOTHING,
                              related_name="questions", verbose_name=_("Board"))
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING,
                              related_name="questions", verbose_name=_("Level"))
    paper = models.ForeignKey(Paper, on_delete=models.DO_NOTHING,
                              related_name="questions", verbose_name=_("Paper"))
    year = models.ForeignKey(Year, on_delete=models.DO_NOTHING,
                             related_name="questions", verbose_name=_("Year"))
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING,
                                related_name="questions", verbose_name=_("Session"))

    tags = TaggableManager()

    ONSAVE_OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(_("Title"), max_length=255)
    excerpt = models.TextField(_("Excerpt"), null=True, blank=True)
    content = models.TextField(_("Content"))
    verified_explanation = models.TextField(
        _("Verified Explanation"), blank=True, null=True)
    # auto_add_now is non-editable
    published = models.DateTimeField(_("Published On"), default=timezone.now)
    updated = models.DateTimeField(
        _("Updated On"), auto_now=True, null=True, blank=True)
    author = models.ForeignKey(
        Accounts, on_delete=models.DO_NOTHING, related_name="questions")
    status = models.CharField(_("Status"),
                              max_length=10, choices=ONSAVE_OPTIONS, default='published')

    search_vector = SearchVectorField(null=True, blank=True)

    class Meta:

        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ('-published',)

        indexes = [
            GinIndex(fields=['search_vector'], name='search_vector_index')
        ]

    def __str__(self):
        return self.title

    slug = AutoSlugField(_("Slug"), populate_from='title',
                         editable=True, unique_with='id')

    ''' Bookmark '''

    FLAG_BOOKMARK = '1'

    def bookmark_add(self, user):
        return self.set_flag(user, status=self.FLAG_BOOKMARK)

    def bookmark_remove(self, user):
        return self.remove_flag(user, status=self.FLAG_BOOKMARK)

    def bookmark_check(self, user):
        return self.is_flagged(user, status=self.FLAG_BOOKMARK)


class Explanation(VoteModel, models.Model):

    class Meta:

        verbose_name = _("Explanation")
        verbose_name_plural = _("Explanations")
        ordering = ('-published',)

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name="explanations", verbose_name=_("Question"))
    content = models.TextField(_("Body"))
    published = models.DateTimeField(_("Published On"), default=timezone.now)
    updated = models.DateTimeField(
        _("Updated On"), auto_now=True, null=True, blank=True)
    author = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, related_name="explanations")
    ONSAVE_OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(_("Status"),
                              max_length=10, choices=ONSAVE_OPTIONS, default='draft')

    def __str__(self):
        return f"Explanation for {self.question} by {self.author}"


class Comment(MPTTModel):
    class MPTTMeta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        order_insertion_by = ['published']

    explanation = models.ForeignKey(Explanation, on_delete=models.CASCADE,
                                    related_name="comments", verbose_name=_("Explanation"))

    parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.CASCADE,
                            related_name="children", verbose_name=_("Parent"))
    content = models.TextField()
    published = models.DateTimeField(_("Published On"), default=timezone.now)
    updated = models.DateTimeField(
        _("Updated On"), auto_now=True, null=True, blank=True)
    author = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, related_name="comments")
    ONSAVE_OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(_("Status"),
                              max_length=10, choices=ONSAVE_OPTIONS, default='draft')

    def __str__(self):
        return f"Comment by {self.author} on {self.explanation}"


@receiver(post_save, sender=Question, dispatch_uid='on_question_save')
def on_question_save(sender, instance, *args, **kwargs):
    sender.objects.filter(pk=instance.id).update(search_vector=(
        SearchVector('title', weight='A') +
        SearchVector('excerpt', weight='A') +
        SearchVector('content', weight='A') +
        SearchVector('verified_explanation', weight='B')
    ))
