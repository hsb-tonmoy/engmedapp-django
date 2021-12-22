from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Teacher
from .serializers import TeacherListSerializer, TeacherSerializer


class TeacherView(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'slug'
    list_serializer_class = TeacherListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(TeacherView, self).get_serializer_class()
