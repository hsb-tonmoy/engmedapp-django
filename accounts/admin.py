from django.contrib import admin
from rest_framework_simplejwt import token_blacklist
from django.contrib.auth.admin import UserAdmin
from .models import Accounts, Profile


class AccountsAdminConfig(UserAdmin):
    model = Accounts

    search_fields = ('email', 'username', 'first_name', 'last_name',)
    list_filter = ('account_type', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('id', 'email', 'username', 'first_name', 'last_name',
                    'is_active', 'is_staff', 'is_verified', 'account_type', 'get_groups')
    fieldsets = (
        (None, {'fields': ('email', 'username',
         'first_name', 'last_name', 'date_joined')}),
        ('Permissions', {'fields': ('account_type',
         'is_staff', 'is_active', 'is_blocked', 'is_verified', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'account_type', 'is_active', 'is_verified', 'is_staff')}
         ),
    )


class ProfileAdminConfig(admin.ModelAdmin):
    model = Profile

    search_fields = ('user',)
    list_filter = ('gender',)
    ordering = ('user',)
    list_display = ('id', 'user', 'date_of_birth', 'gender', 'last_login')
    fieldsets = (
        (None, {'fields': ('user', 'profile_pic', 'is_public',
         'date_of_birth', 'gender', 'pronouns', 'last_login', 'user_rep')}),
        ('Address', {'fields': ('city', 'state', 'country',)}),
        ('Teacher', {'fields': ('name_of_institution',
         'phone_no', 'email_address', 'website_url')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'is_public', 'profile_pic', 'date_of_birth', 'gender', 'pronouns', 'city', 'state', 'country', 'name_of_institution', 'phone_no', 'email_address', 'website_url')}
         ),
    )


admin.site.register(Accounts, AccountsAdminConfig)
admin.site.register(Profile, ProfileAdminConfig)


class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken,
                    OutstandingTokenAdmin)
