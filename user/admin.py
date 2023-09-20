from django.contrib import admin
from .models import AuthUser, Order, Like
from django.contrib.auth.models import Group, User

admin.site.unregister([Group])
admin.site.register([AuthUser, Order, Like])