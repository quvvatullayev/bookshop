from django.contrib import admin
from .models import Category, Product, Advertisement

admin.site.register([Category, Product, Advertisement])