# Generated by Django 3.1.8 on 2021-08-15 06:30

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('question_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUIDTaggedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.UUIDField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_db_uuidtaggeditem_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_db_uuidtaggeditem_items', to='taggit.tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='question_db.UUIDTaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
