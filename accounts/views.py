from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from .serializers import CookieTokenRefreshSerializer, ProfileSerializer
from .models import Profile
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import BasePermission, SAFE_METHODS

# JWT Cookie Start


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 10  # 10 days
            response.set_cookie(
                'refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True)
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = 3600 * 24 * 10  # 10 days
            response.set_cookie(
                'refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True)
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)
    serializer_class = CookieTokenRefreshSerializer


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def delete_auth_cookies(self, response, refresh_token):
        response.set_cookie(
            'refresh_token',
            refresh_token,
            max_age=1,
            httponly=True
        )

    def post(self, request):
        response = Response({})
        try:
            refresh_token = request.COOKIES['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            self.delete_auth_cookies(response, refresh_token)
            return response
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# JWT Cookie End


class ProfilePermissions(BasePermission):
    message = "Editing profile is restricted to the owner only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user or (request.user.account_type == 5)


class ProfileView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [
        DjangoModelPermissionsOrAnonReadOnly, ProfilePermissions]
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
