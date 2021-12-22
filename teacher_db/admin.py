from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email_address')
    list_filter = ('gender', 'location', 'time_zone',)
    ordering = ('first_name',)
    list_display = ('first_name', 'last_name', 'slug', 'email_address', 'location',
                    'time_zone', 'phone_no', 'institute',)
