from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AccountsSerializer
from rest_framework.permissions import AllowAny


class AccountRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
