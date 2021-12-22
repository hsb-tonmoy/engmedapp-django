# Generated by Django 3.1.8 on 2021-12-22 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('trash', 'Trash')], default='published', max_length=10, verbose_name='Status')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Other'), (4, 'Prefer Not to Answer')], null=True, verbose_name='Gender')),
                ('location', models.CharField(blank=True, max_length=510, null=True, verbose_name='Location')),
                ('time_zone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Time Zone')),
                ('phone_no', models.CharField(blank=True, max_length=25, null=True, verbose_name='Phone Number')),
                ('email_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email Address')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('social_media', models.JSONField(blank=True, null=True, verbose_name='Social Media')),
                ('institute', models.CharField(blank=True, max_length=510, null=True, verbose_name='Institute')),
                ('qualification', models.TextField(blank=True, null=True, verbose_name='Qualification')),
                ('highest_degree', models.CharField(blank=True, max_length=255, null=True, verbose_name='Highest Degree')),
                ('subjects_taught', models.TextField(blank=True, null=True, verbose_name='Subjects Taught')),
                ('years_experience', models.CharField(blank=True, max_length=10, null=True, verbose_name='Years of experience')),
                ('students_taught', models.CharField(blank=True, max_length=10, null=True, verbose_name='Students Taught')),
                ('preferred_mode_of_teaching', models.CharField(blank=True, max_length=255, null=True, verbose_name='Preferred mode of teaching')),
                ('preferred_mode_of_payment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Preferred mode of payment')),
                ('preferred_language', models.CharField(blank=True, max_length=255, null=True, verbose_name='Preferred Language')),
                ('special_note', models.TextField(blank=True, null=True, verbose_name='Special Note')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teacher_db', to=settings.AUTH_USER_MODEL, verbose_name='Account')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
                'ordering': ['id'],
            },
        ),
    ]
