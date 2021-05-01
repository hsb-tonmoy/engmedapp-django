from media_lib.models import Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    image_thumb = serializers.ImageField(required=False)
    image_med = serializers.ImageField(required=False)
    image_large = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = "__all__"
