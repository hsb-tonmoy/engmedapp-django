from rest_framework import serializers
from accounts.serializers import AccountSerializer
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    account = AccountSerializer(required=False, many=False, read_only=False)
    profile_pic = serializers.ImageField(required=False)

    class Meta:
        model = Teacher
        fields = '__all__'
