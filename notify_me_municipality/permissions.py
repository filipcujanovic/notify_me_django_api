from rest_framework import permissions

class AllowOnlyUserMunicipalities(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id