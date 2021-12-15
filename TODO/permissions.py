from rest_framework import permissions
from .models import *





class ISOwner(permissions.BasePermission):
   
    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and request.user.is_superuser:
            return True
        if request.method == 'DELETE' and request.user.is_superuser:
            return obj.delete()
        else:
            return obj.owner == request.user




