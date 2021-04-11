# Generated by Django 3.1.7 on 2021-04-04 07:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_db', '0002_auto_20210404_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from=('title', 'id'), unique_with=('id',), verbose_name='Slug'),
        ),
    ]
