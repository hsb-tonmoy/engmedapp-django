from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='image_thumb')
    list_display = ('id', 'admin_thumbnail',
                    'file_name', 'alt_tag', 'uploaded')


admin.site.register(Image, ImageAdmin)
