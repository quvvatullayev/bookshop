from django import forms
from .models import AuthUser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = AuthUser
        fields = ('username', 'tg_name', 'phone')