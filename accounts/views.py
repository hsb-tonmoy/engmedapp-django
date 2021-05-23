from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from .serializers import CookieTokenRefreshSerializer, ProfileSerializer
from .models import Profile
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.conf import settings

# Social Imports
from rest_social_auth.views import *
from rest_social_auth.serializers import JWTPairSerializer
from social_django.utils import load_backend, load_strategy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

# JWT Cookie Start


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = settings.COOKIE_AGE  # 10 days
            response.set_cookie(
                'refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True)
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = settings.COOKIE_AGE  # 10 days
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


class AuthorizationURL(CreateAPIView):
    def get(self, request, *args, **kwargs):
        redirect_uri = request.GET.get("redirect_uri")
        if redirect_uri != settings.REST_SOCIAL_OAUTH_ABSOLUTE_REDIRECT_URI:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        strategy = load_strategy(request)
        strategy.session_set("redirect_uri", redirect_uri)

        backend_name = self.kwargs["provider"]
        backend = load_backend(strategy, backend_name,
                               redirect_uri=redirect_uri)

        authorization_url = backend.auth_url()
        return Response(data={"authorization_url": authorization_url})


class SocialJWTPairOnlyAuthView(SimpleJWTAuthMixin, BaseSocialAuthView):
    serializer_class = JWTPairSerializer

    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        cookie_max_age = settings.COOKIE_AGE  # 10 days
        input_data = self.get_serializer_in_data()
        provider_name = self.get_provider_name(input_data)
        if not provider_name:
            return self.respond_error("Provider is not specified")
        self.set_input_data(request, input_data)
        decorate_request(request, provider_name)
        serializer_in = self.get_serializer_in(data=input_data)
        if self.oauth_v1() and request.backend.OAUTH_TOKEN_PARAMETER_NAME not in input_data:
            # oauth1 first stage (1st is get request_token, 2nd is get access_token)
            manual_redirect_uri = self.request.auth_data.pop(
                'redirect_uri', None)
            manual_redirect_uri = self.get_redirect_uri(manual_redirect_uri)
            if manual_redirect_uri:
                self.request.backend.redirect_uri = manual_redirect_uri
            request_token = parse_qs(request.backend.set_unauthorized_token())
            response = Response(request_token)
            response.set_cookie(
                'refresh_token', request_token, max_age=cookie_max_age, httponly=True)
            return response
        serializer_in.is_valid(raise_exception=True)
        try:
            user = self.get_object()
        except (AuthException, HTTPError) as e:
            return self.respond_error(e)
        if isinstance(user, HttpResponse):
            # error happened and pipeline returned HttpResponse instead of user
            return user
        resp_data = self.get_serializer(instance=user)
        refresh_token = resp_data.data['refresh']
        self.do_login(request.backend, user)
        res = Response(resp_data.data)
        res.set_cookie(
            'refresh_token', refresh_token, max_age=cookie_max_age, httponly=True)
        return res


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
