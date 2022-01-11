# Generated by Django 3.1.8 on 2021-12-03 21:08

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_db', '0003_remove_explanation_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='question',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='search_vector_index'),
        ),
    ]