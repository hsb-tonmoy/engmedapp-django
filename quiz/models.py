from django.db import models
from django.db.models.fields import related
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField

# Create your models here.


class Categories(MPTTModel, models.Model):
    class Meta:

        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["tree_id", "lft"]

    name = models.CharField(max_length=255)
    parent = TreeForeignKey("self", blank=True, null=True,
                            on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Quizzes(models.Model):

    class Meta:

        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))
    no_of_attempts = models.IntegerField(
        default=1, verbose_name=_("Number of Attempts"))
    categories = TreeManyToManyField(Categories, verbose_name=_("Categories"))

    def __str__(self):
        return self.title

    def get_categories(self):
        return ", ".join([str(cat) for cat in self.categories.all()])


class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):

    class Meta:

        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    TYPE = (
        (0, _("Multiple Choice")),
        (1, _("True or False")),
        (2, _("Blanks")),
        (3, _("Essay")),
    )

    quiz = models.ForeignKey(
        Quizzes, related_name="question", on_delete=models.DO_NOTHING)

    type_of = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type of Question"))

    title = models.TextField(verbose_name=_("Title"))

    date_created = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(
        default=True, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answer(Updated):
    question = models.ForeignKey(
        Question, related_name="answer", on_delete=models.DO_NOTHING)

    answer_text = models.TextField(
        verbose_name=_("Answer Text"), default="Answer")

    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
