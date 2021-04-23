from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'user_name',
                  'full_name', 'password', 'account_type')


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['user'] = user.user_name
#         token['account_type'] = user.account_type

#         return token
