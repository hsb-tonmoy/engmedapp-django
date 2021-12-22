from rest_framework import serializers
from accounts.serializers import AccountSerializer
from .models import Teacher


class TeacherListSerializer(serializers.ModelSerializer):

    profile_pic = serializers.ImageField(required=False)

    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = Teacher
        fields = ('id', 'slug', 'profile_pic', 'name',
                  'institute', 'subjects_taught', 'location', 'time_zone', )


class TeacherSerializer(serializers.ModelSerializer):

    account = AccountSerializer(required=False, many=False, read_only=False)
    profile_pic = serializers.ImageField(required=False)

    class Meta:
        model = Teacher
        fields = '__all__'
