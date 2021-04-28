# Generated by Django 3.1.8 on 2021-04-27 23:47

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
