from rest_framework import generics
from ..models import Product 
from ..serialization import ProductSerializer
from rest_framework.response import Response
from django.contrib import messages
from ..models import Category
from ..serialization import CategorySerializer
from .advertisement import Advertisement, AdvertisementSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser|ReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book_name', 'author_book', 'category']
    

    def list(self, request, *args, **kwargs):
        products_obj = Product.objects.all()
        products = ProductSerializer(products_obj, many = True).data

        new_product_obj = Product.objects.all()[:10]
        new_product = ProductSerializer(new_product_obj, many = True).data

        advertisement_obj = Advertisement.objects.all()
        advertisement = AdvertisementSerializer(advertisement_obj, many = True).data
        
        data = {
            'products':products,
            'new_products':new_product,
            'advertisements':advertisement,
        }
        categorys_obj = Category.objects.all()
        categorys = CategorySerializer(categorys_obj, many = True).data

        data = {
            'products':products,
            'new_products':new_product,
            'advertisements':advertisement,
            'categorys':categorys,
        }

        for i in categorys:
            product_obj = Product.objects.filter(category = i['id'])
            product = ProductSerializer(product_obj, many = True).data
            data[i['category_name']] = product

        return Response(data=data)

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser|ReadOnly]

    def update(self, request, *args, **kwargs):
        messages.success(self.request, "this book has been updated.", extra_tags='success')
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        messages.success(self.request, "this book has been delete.", extra_tags='success')
        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        product_obj = Product.objects.get(id = kwargs['pk'])
        product = ProductSerializer(product_obj, many=False).data
        author_book = product['author_book']

        author_book_obj = Product.objects.filter(author_book = author_book)
        author_book = ProductSerializer(author_book_obj, many = True).data

        category_book_obj = Product.objects.filter(category = product['category'])
        category_book = ProductSerializer(category_book_obj, many = True).data[:10]

        data = {
            'product':product,
            'author_books':author_book,
            'category_books':category_book
        }
        
        return Response(data = data)
