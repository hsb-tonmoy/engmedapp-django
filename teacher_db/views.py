from rest_framework import generics, viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherView(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
