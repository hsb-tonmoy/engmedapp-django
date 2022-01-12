from django.contrib.postgres.search import SearchVector
from django.db import migrations


def update_search_vector(apps, schema_editor):
    Question = apps.get_model('question_db', 'Question')
    Question.objects.all().update(search_vector=(
        SearchVector('title', weight='A') +
        SearchVector('excerpt', weight='A') +
        SearchVector('content', weight='A') +
        SearchVector('verified_explanation', weight='B')
    ))


class Migration(migrations.Migration):

    dependencies = [
        ('question_db', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_search_vector, elidable=True),
    ]
