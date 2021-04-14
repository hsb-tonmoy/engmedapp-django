from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from autoslug import AutoSlugField
from accounts.models import Accounts


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


class Question(models.Model):

    class Meta:

        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ('-published',)

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

    ONSAVE_OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(_("Title"), max_length=255)
    excerpt = models.TextField(_("Excerpt"), null=True, blank=True)
    content = models.TextField(_("Content"),)
    # auto_add_now is non-editable
    published = models.DateTimeField(_("Published On"), default=timezone.now)
    updated = models.DateTimeField(
        _("Updated On"), auto_now=True, null=True, blank=True)
    author = models.ForeignKey(
        Accounts, on_delete=models.DO_NOTHING, related_name="questions")
    status = models.CharField(_("Status"),
                              max_length=10, choices=ONSAVE_OPTIONS, default='published')

    def __str__(self):
        return self.title

    slug = AutoSlugField(_("Slug"), populate_from='title',
                         editable=True, unique_with='id')

    # def get_absolute_url(self):
    #     return reverse('question', kwargs={'slug': self.slug, 'id':self.id})


class Explanation(models.Model):

    class Meta:

        verbose_name = _("Explanation")
        verbose_name_plural = _("Explanations")
        ordering = ('-published',)

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name="explanations", verbose_name=_("Question"))
    excerpt = models.TextField(_("Excerpt"), null=True, blank=True)
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
