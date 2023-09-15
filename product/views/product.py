from rest_framework import generics
from ..models import Product 
from ..serialization import ProductSerializer
from rest_framework.response import Response

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        product_obj = Product.objects.get(id = kwargs['pk'])
        product = ProductSerializer(product_obj, many=False).data
        author_name = product['author_name']

        author_book_obj = Product.objects.filter(author_name = author_name)
        author_book = ProductSerializer(author_book_obj, many = True).data

        category_book_obj = Product.objects.filter(category = product['category'])
        category_book = ProductSerializer(category_book_obj, many = True).data[:10]

        data = {
            'product':product,
            'author_books':author_book,
            'category_books':category_book
        }
        
        return Response(data = data)
