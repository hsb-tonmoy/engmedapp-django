from accounts.models import Profile
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

User = get_user_model()


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken(
                'No valid token found in cookie \'refresh_token\'')


class UserCreateSerializer(UserCreateSerializer):
    profile_pic = serializers.ImageField(source="profile.profile_pic")

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'user_name',
                  'full_name', 'password', 'account_type', 'profile_pic')


class ProfileSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = "__all__"
