from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit import ImageSpec, register
from .processors import ImageThumbSpec, ImageMedSpec, ImageLargeSpec
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from random import randint


register.generator('media_lib:imagethumb', ImageThumbSpec)
register.generator('media_lib:imagemed', ImageMedSpec)
register.generator('media_lib:imagelarge', ImageLargeSpec)


def upload_to_path(instance, filename):
    file_name = filename.split(".")[0][:30]
    file_id = randint(10000000, 99999999)
    path = f'images/{file_id}_{file_name}.png'
    return path


class Image(models.Model):

    image = ProcessedImageField(upload_to=upload_to_path,
                                format='PNG',
                                options={'quality': 60})
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

    if default_storage.exists(thumb):

        default_storage.delete(thumb)
