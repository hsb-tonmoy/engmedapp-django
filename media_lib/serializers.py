from media_lib.models import Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    image_thumb = serializers.ImageField()
    image_med = serializers.ImageField()
    image_large = serializers.ImageField()

    class Meta:
        model = Image
        fields = "__all__"
