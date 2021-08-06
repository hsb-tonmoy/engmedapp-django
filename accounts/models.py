from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from random import randint


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_blocked', False)
        other_fields.setdefault('account_type', 5)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, last_name, password, **other_fields)

    def create_user(self, email, first_name=None, last_name=None, password=None, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Accounts(AbstractBaseUser, PermissionsMixin):
    class Meta:

        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    email = models.EmailField(_('Email Address'), unique=True)
    username = models.CharField(
        _('Username'), max_length=50, blank=True, null=True, unique=True)
    first_name = models.CharField(_('First Name'), max_length=255, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=255, blank=True)
    date_joined = models.DateTimeField(_("Join Date"), default=timezone.now)
    is_staff = models.BooleanField(_("Is the User a Staff?"), default=False)
    is_active = models.BooleanField(_("Is the User Active?"), default=False)
    is_verified = models.BooleanField(
        _("Is the Teacher Verified?"), default=False)
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

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.username}"

    def get_email(self):
        return self.email

    def get_groups(self):
        return "\n".join([p.name for p in self.groups.all()])


def upload_to_path(instance, filename):
    extension = filename.split(".")[-1].lower()
    file_id = randint(10000000, 99999999)
    path = f'profiles/{file_id}_{instance.user.username}.png'
    return path


class Profile(models.Model):
    user = models.OneToOneField(
        Accounts, on_delete=models.CASCADE, related_name="profile")
    is_public = models.BooleanField(
        _("Is the profile public or private?"), default=True)
    profile_pic = ProcessedImageField(upload_to=upload_to_path,
                                      processors=[ResizeToFill(270, 260)],
                                      format='PNG',
                                      options={'quality': 60}, default='profiles/avatar.png', null=True, blank=True)
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
    country = models.CharField(
        _("Country"), max_length=50, blank=True, null=True)

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


@receiver(post_save, sender=Accounts)
def add_or_update_user_group(sender, instance, created, **kwargs):
    if created:
        if instance.account_type == 1 or instance.account_type == 2:
            group = Group.objects.get(name="Students and Teachers")
        elif instance.account_type == 3:
            group = Group.objects.get(name="Content Creator")
        elif instance.account_type == 4:
            group = Group.objects.get(name="Manager")
        elif instance.account_type == 5 or instance.is_superuser:
            if not Group.objects.filter(name="Admin").exists():
                Group.objects.create(name="Admin")
            group = Group.objects.get(name="Admin")

        instance.groups.add(group)


@receiver(post_save, sender=Accounts)
def send_mail_on_create(sender, instance, created, **kwargs):

    subject = 'Welcome to EngMedApp - Thank Your For Signing Up'
    from_email = 'no-reply@engmedapp.com'
    message = 'Thank Your For Signing Up'
    recepient_list = [instance.email]
    html_message = '<h1>Thank Your For Signing Up</h1>'

    if created:
        send_mail(subject, message, from_email, recepient_list,
                  fail_silently=False, html_message=html_message)
