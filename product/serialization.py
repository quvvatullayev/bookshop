from rest_framework import serializers
from .models import (
    Category,
    Product,
    Advertisement,
    AuthorBook
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'

class AuthorBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBook
        fields = '__all__'