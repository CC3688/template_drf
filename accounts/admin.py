from django.contrib import admin

from .models import User, Role, Permission, RolePermission
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(RolePermission)
