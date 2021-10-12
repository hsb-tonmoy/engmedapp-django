from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from .serializers import AccountSerializer, ProfileSerializer
from .models import Accounts, Profile
from rest_framework import status, viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import SAFE_METHODS
from djoser.permissions import CurrentUserOrAdmin

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


class ProfilePermissions(IsAuthenticatedOrReadOnly):
    message = "Editing profile is restricted to the owner only."

    def has_object_permission(self, request, view, obj):

        user = request.user

        if type(obj) == type(user) and obj.pk == user.pk:
            return True

        return request.method in SAFE_METHODS or user.is_staff


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = [
        IsAuthenticated, ProfilePermissions]
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    lookup_field = "user__username"

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


class AccountView(RetrieveUpdateAPIView):
    queryset = Accounts.objects.all()
    permission_classes = [CurrentUserOrAdmin]
    serializer_class = AccountSerializer
