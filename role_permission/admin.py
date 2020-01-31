from django.contrib import admin

from .models import Role, Permission

# Register your models here.


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_permissions')

    def get_permissions(self, obj):
        return ", ".join([p.name for p in obj.permissions.all()])

    get_permissions.short_description = 'Permissions'


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', )