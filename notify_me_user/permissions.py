from rest_framework import permissions


class AllowPostAnyReadAuthenticatedUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        else:
            return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_superuser