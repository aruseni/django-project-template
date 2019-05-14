from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from django.utils.translation import ugettext_lazy as _

from .forms import UserChangeForm, UserCreationForm

from .models import User


class AdminSite(admin.AdminSite):
    site_header = _('Admin')


admin_site = AdminSite(name='admin')


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'date_joined', 'is_staff')
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'groups',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name')}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)


admin_site.register(User, MyUserAdmin)
