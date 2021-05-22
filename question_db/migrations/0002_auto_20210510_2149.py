# Generated by Django 3.1.8 on 2021-05-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='explanation',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='explanation',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='explanation',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]