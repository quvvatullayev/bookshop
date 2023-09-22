from rest_framework import generics
from ..models import AuthUser
from ..serialization import AuthUserSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthUserListCreateView(generics.ListCreateAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

class AuthUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS