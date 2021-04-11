from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, full_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, full_name, password, **other_fields)

    def create_user(self, email, user_name, full_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          full_name=full_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Accounts(AbstractBaseUser, PermissionsMixin):
    class Meta:

        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    email = models.EmailField(_('Email Address'), unique=True)
    user_name = models.CharField(_('Username'), max_length=50, unique=True)
    full_name = models.CharField(_('Full Name'), max_length=255, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(_("Date of Birth"), null=True, blank=True)
    date_joined = models.DateTimeField(_("Join Date"), default=timezone.now)
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
        (4, 'Prefer Not to Answer'),
    )
    gender = models.PositiveSmallIntegerField(
        _("Gender"), choices=GENDER, null=True, blank=True)
    last_login = models.DateTimeField(
        _("Last Logged-in"), null=True, blank=True)
    is_staff = models.BooleanField(_("Is the User a Staff?"), default=False)
    is_active = models.BooleanField(_("Is the User Active?"), default=False)
    is_public = models.BooleanField(
        _("Is the profile public or private?"), default=True)
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher'),
        (3, 'Content Creator'),
        (4, 'Manager'),
        (5, 'Admin'),
    )

    account_type = models.PositiveSmallIntegerField(
        _("Account Type"), choices=USER_TYPE_CHOICES, default=1)

    ''' Teacher's Fields Start '''

    name_of_institution = models.CharField(_("Name of Institution"),
                                           max_length=255, null=True, blank=True)
    phone_no = models.CharField(
        _("Phone Number"), max_length=255, null=True, blank=True)
    email_address = models.CharField(
        _("Contact Email Address"), max_length=255, null=True, blank=True)
    website_url = models.URLField(
        _("Website URL"), max_length=255, null=True, blank=True)

    ''' Teacher's Fields End '''

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'full_name']

    def __str__(self):
        return self.full_name

    def get_email(self):
        return self.email
