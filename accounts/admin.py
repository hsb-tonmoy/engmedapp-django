from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Accounts

# Register your models here.


class AccountsAdminConfig(UserAdmin):
    model = Accounts

    search_fields = ('email', 'user_name', 'full_name',)
    list_filter = ('account_type', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'user_name', 'full_name',
                    'is_active', 'is_staff', 'account_type')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'full_name', 'date_joined')}),
        ('Permissions', {'fields': ('account_type', 'is_staff', 'is_active')}),
        ('Personal', {'fields': ('date_of_birth', 'gender', 'profile_pic',
         'name_of_institution', 'phone_no', 'email_address', 'website_url')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'full_name', 'password1', 'password2', 'account_type', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Accounts, AccountsAdminConfig)
