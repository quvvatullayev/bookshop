from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from django.contrib.auth.models import User

class IsAdminUser(BasePermission):
    # def has_permission(self, request:Request, view):
    #     user:User = request.user
    #     if user.is_authenticated:
    #         return False
    #     return True
        
    def has_permission(self, request:Request, view):
        user:User = request.user
        if user.is_authenticated and user.is_staff and request.method in SAFE_METHODS:
            return True
        else:
            return False