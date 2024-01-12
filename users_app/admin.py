from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, PasswordReset

# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'mobile')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login','date_joined',)}),
        (('user_info'), {'fields': ('location','role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'mobile', 'location', 'role']
    search_fields = ('email', 'first_name', 'last_name', 'mobile', 'location', 'role')
    ordering = ('email', )

admin.site.register(User, UserAdmin)
admin.site.register(PasswordReset)