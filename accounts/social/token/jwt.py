from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings


class TokenStrategy:
    @classmethod
    def obtain(cls, user):

        response = Response({})

        refresh_token = RefreshToken.for_user(user)

        cookie_max_age = settings.COOKIE_AGE

        response.set_cookie(
            'refresh_token', refresh_token, max_age=cookie_max_age, httponly=True)

        return response
