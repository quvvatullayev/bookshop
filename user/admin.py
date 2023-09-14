from django.contrib import admin
from .models import AuthUser, Order, Like

admin.site.register([AuthUser, Order, Like])