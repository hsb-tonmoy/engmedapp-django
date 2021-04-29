from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit import register
from .processors import ImageThumbSpec, ImageMedSpec, ImageLargeSpec
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from random import randint
from datetime import date

register.generator('media_lib:imagethumb', ImageThumbSpec)
register.generator('media_lib:imagemed', ImageMedSpec)
register.generator('media_lib:imagelarge', ImageLargeSpec)


def upload_to_path(instance, filename):
    file_name = filename.split(".")[0][:30]
    extension = filename.split(".")[-1]
    file_id = randint(10000000, 99999999)
    today = date.today()
    upload_date = today.strftime("%d_%m_%Y").split("_")
    path = f'images/{upload_date[2]}/{upload_date[1]}/{upload_date[0]}/{file_name}_{file_id}.{extension}'
    return path


class Image(models.Model):

    image = ProcessedImageField(upload_to=upload_to_path,
                                options={'quality': 50})
    image_thumb = ImageSpecField(source='image',
                                 id='media_lib:imagethumb')
    image_med = ImageSpecField(source='image',
                               id='media_lib:imagemed')
    image_large = ImageSpecField(source='image',
                                 id='media_lib:imagelarge')
    file_name = models.CharField(_("File Name"), max_length=255)
    alt_tag = models.CharField(_("Alt Tag"), max_length=255)
    uploaded = models.DateTimeField(_("Uploaded At"), default=timezone.now)

    class Meta:

        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordering = ["-uploaded"]


@receiver(post_delete, sender=Image)
def delete_images(sender, instance, **kwargs):

    thumb = str(instance.image_thumb)
    med = str(instance.image_med)
    large = str(instance.image_large)

    if default_storage.exists(thumb):

        default_storage.delete(thumb)

    if default_storage.exists(med):

        default_storage.delete(med)

    if default_storage.exists(large):

        default_storage.delete(large)
