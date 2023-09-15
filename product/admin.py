from django.contrib import admin
from .models import Category, Product, Advertisement,AuthorBook

admin.site.register([Category, Product, Advertisement, AuthorBook])