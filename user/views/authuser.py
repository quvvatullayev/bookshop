from rest_framework import generics
from ..models import AuthUser
from ..serialization import AuthUserSerializer, SingupFormSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS
from ..forms import SignupForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User

class AuthUserListCreateView(generics.ListCreateAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

class AuthUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

class ReadOnly(BasePermission):
    def has_object_permission(self, request:Request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user:User = request.user
        return user.is_staff == True

class SingUpView(APIView):
    def post(self, request):
        form = SignupForm(data = request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return Response({'singup':form.data})
        return Response({'singup':'error'})
    

    
