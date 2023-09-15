from rest_framework import generics
from ..models import AuthUser
from ..serialization import AuthUserSerializer

class AuthUserListCreateView(generics.ListCreateAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

class AuthUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer