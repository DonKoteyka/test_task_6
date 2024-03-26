from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user == obj.creator or request.user.is_superuser

