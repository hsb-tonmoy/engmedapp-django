from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, full_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_blocked', False)

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
    date_joined = models.DateTimeField(_("Join Date"), default=timezone.now)
    is_staff = models.BooleanField(_("Is the User a Staff?"), default=False)
    is_active = models.BooleanField(_("Is the User Active?"), default=False)
    is_blocked = models.BooleanField(_("Is the User Blocked?"), default=False)
    USER_TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Teacher'),
        (3, 'Content Creator'),
        (4, 'Manager'),
        (5, 'Admin'),
    )

    account_type = models.PositiveSmallIntegerField(
        _("Account Type"), choices=USER_TYPE_CHOICES, default=1)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'full_name']

    def __str__(self):
        return self.full_name

    def get_email(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        Accounts, on_delete=models.CASCADE, related_name="profile")
    is_public = models.BooleanField(
        _("Is the profile public or private?"), default=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(_("Date of Birth"), null=True, blank=True)
    GENDER = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
        (4, 'Prefer Not to Answer'),
    )
    gender = models.PositiveSmallIntegerField(
        _("Gender"), choices=GENDER, null=True, blank=True)
    pronouns = models.CharField(
        _("Pronouns"), max_length=30, blank=True, null=True)
    last_login = models.DateTimeField(
        _("Last Logged-in"), null=True, blank=True)

    user_rep = models.IntegerField(_("User Reputation"), default=0)

    '''Address'''

    city = models.CharField(_("City"), max_length=100, blank=True, null=True)
    state = models.CharField(_("State"), max_length=50, blank=True, null=True)
    country = CountryField(blank_label='(Select Country)')

    ''' Teacher's Fields Start '''

    name_of_institution = models.CharField(_("Name of Institution"),
                                           max_length=255, null=True, blank=True)
    phone_no = models.CharField(
        _("Phone Number"), max_length=255, null=True, blank=True)
    email_address = models.CharField(
        _("Contact Email Address"), max_length=255, null=True, blank=True)
    website_url = models.URLField(
        _("Website URL"), max_length=255, null=True, blank=True)


@receiver(post_save, sender=Accounts)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
