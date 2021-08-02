from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.conf import settings

# JWT Cookie Start


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
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
