from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as ContribUserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(ContribUserAdmin):
    # override all [..., 'first_name', 'last_name', ...] => [..., 'full_name', ...] from ancestor class
    fieldsets = [
        (None, {'fields': ['username', 'password']}),
        (_("Personal info"), {'fields': ['full_name', 'email']}),
        (_("Permissions"), {'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']}),
        (_("Important dates"), {'fields': ['last_login', 'date_joined']}),
    ]
    list_display = ['username', 'email', 'full_name', 'is_staff']
    search_fields = ['username', 'full_name', 'email']
