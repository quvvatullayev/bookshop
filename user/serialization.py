from rest_framework import serializers
from .models import AuthUser, Order, Like
from .forms import SignupForm

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class SingupFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignupForm
        fields = '__all__'

        