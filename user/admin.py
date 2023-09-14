from django.contrib import admin
from .models import AuthUser, Order

admin.site.register([AuthUser, Order])