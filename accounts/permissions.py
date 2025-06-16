from rest_framework.permissions import BasePermission

class HasPermission(BasePermission):
    def has_permission(self, request, view):
        required_permission = getattr(view, 'required_permission', None)
        if not required_permission:
            return True

        user = request.user
        if not user.is_authenticated:
            return False

        user_permissions = set()
        for role in user.roles.all():
            perms = role.rolepermission_set.all().values_list('permission__codename', flat=True)
            user_permissions.update(perms)

        return required_permission in user_permissions
