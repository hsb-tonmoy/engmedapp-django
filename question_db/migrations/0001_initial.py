# Generated by Django 3.1.8 on 2021-05-23 21:03

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Paper',
                'verbose_name_plural': 'Papers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Year',
                'verbose_name_plural': 'Years',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('excerpt', models.TextField(blank=True, null=True, verbose_name='Excerpt')),
                ('content', models.TextField(verbose_name='Content')),
                ('verified_explanation', models.TextField(blank=True, null=True, verbose_name='Verified Explanation')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published On')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated On')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10, verbose_name='Status')),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique_with=('id',), verbose_name='Slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to='question_db.board', verbose_name='Board')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to='question_db.level', verbose_name='Level')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to='question_db.paper', verbose_name='Paper')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to='question_db.session', verbose_name='Session')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='questions', to='question_db.year', verbose_name='Year')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('excerpt', models.TextField(blank=True, null=True, verbose_name='Excerpt')),
                ('content', models.TextField(verbose_name='Body')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published On')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated On')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='explanations', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='explanations', to='question_db.question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Explanation',
                'verbose_name_plural': 'Explanations',
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published On')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated On')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Status')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('explanation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='question_db.explanation', verbose_name='Explanation')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='question_db.comment', verbose_name='Parent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
