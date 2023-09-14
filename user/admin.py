from django.contrib import admin
from .models import AuthUser, Order, Like
from django.contrib.auth.models import Group

admin.site.unregister([Group])
admin.site.register([AuthUser, Order, Like])