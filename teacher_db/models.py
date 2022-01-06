import uuid
from django.db import models
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from random import randint

from accounts.models import Accounts


class Teacher(models.Model):
    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")
        ordering = ["id"]

    ONSAVE_OPTIONS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('trash', 'Trash'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING, blank=True, null=True,
                                related_name="teacher_db", verbose_name=_("Account"))

    slug = AutoSlugField(_("Slug"), populate_from=['first_name', 'last_name'],
                         editable=True, unique_with=['first_name', 'last_name'])

    status = models.CharField(_("Status"),
                              max_length=10, choices=ONSAVE_OPTIONS, default='published')

    # Personal Information

    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    date_of_birth = models.DateField(_("Date of Birth"), null=True, blank=True)

    def upload_to_path(instance, filename):
        extension = filename.split(".")[-1].lower()
        file_id = randint(10000000, 99999999)
        path = f'teachers/{file_id}_{instance.first_name}.png'
        return path

    profile_pic = ProcessedImageField(upload_to=upload_to_path,
                                      processors=[ResizeToFill(270, 270)],
                                      format='PNG',
                                      options={'quality': 60}, default='profiles/avatar.png', null=True, blank=True)

    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
        (4, 'Prefer Not to Answer'),
    )
    gender = models.PositiveSmallIntegerField(
        _("Gender"), choices=GENDER, null=True, blank=True)

    location = models.CharField(
        _('Location'), max_length=510, null=True, blank=True)

    time_zone = models.CharField(
        _('Time Zone'), max_length=255, null=True, blank=True)

    # Communication

    phone_no = models.CharField(
        _('Phone Number'), max_length=25, blank=True, null=True)

    email_address = models.CharField(
        _('Email Address'), max_length=255, blank=True, null=True)

    website = models.CharField(
        _('Website'), max_length=255, blank=True, null=True)

    social_media = models.JSONField(_('Social Media'), blank=True, null=True)

    # Academic Information

    institute = models.CharField(
        _('Institute'), max_length=510, blank=True, null=True)

    qualification = models.TextField(
        _('Qualification'), blank=True, null=True)

    highest_degree = models.CharField(
        _('Highest Degree'), max_length=255, blank=True, null=True)

    # Tuition Information

    working_experience = models.TextField(
        _('Working Experience'), blank=True, null=True)

    subjects_taught = models.TextField(
        _('Subjects Taught'), blank=True, null=True)

    years_experience = models.CharField(
        _('Years of experience'), max_length=10, blank=True, null=True)

    students_taught = models.CharField(
        _('Students Taught'), max_length=10, blank=True, null=True)

    preferred_mode_of_teaching = models.CharField(
        _('Preferred mode of teaching'), max_length=255, blank=True, null=True)  # online, offline, both

    expected_salary = models.CharField(
        _('Expected salary'), max_length=255, blank=True, null=True)

    preferred_mode_of_payment = models.CharField(
        _('Preferred mode of payment'), max_length=255, blank=True, null=True)  # $amount + per hour / per lecture / per month

    preferred_language = models.CharField(
        _('Preferred Language'), max_length=255, blank=True, null=True)

    hour_of_operation = models.CharField(
        _('Hour pf operation'), max_length=255, blank=True, null=True)

    special_note = models.TextField(
        _('Special Note'), blank=True, null=True)
