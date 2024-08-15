from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.accounts import User
from .models.tasks import Task


class UserAdminConfig(UserAdmin):

    model = User
    list_display = ('email', 'username', 'is_superuser','is_staff', 'is_active',)
    list_filter = ('email', 'username', 'is_superuser','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','name','email', 'password')}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'name',
                'password1',
                'password2',
                'is_superuser',
                'is_staff',
                'is_active'
                )
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, UserAdminConfig)
admin.site.register(Task)
