from rest_framework import generics
from ..models import AuthorBook, Product
from ..serialization import AuthorBooksSerializer, ProductSerializer
from rest_framework.response import Response

class AuthorBooksListCreateView(generics.ListCreateAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBooksSerializer

class AuthorBookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorBook
    serializer_class = AuthorBooksSerializer

    def retrieve(self, request, *args, **kwargs):
        authorbook_obj = AuthorBook.objects.get(id = kwargs['pk'])
        authorbook = AuthorBooksSerializer(authorbook_obj, many = False).data

        product_obj = Product.objects.filter(author_book = authorbook['id'])
        product = ProductSerializer(product_obj, many = True).data
        
        data = {
            'authorbook':authorbook,
            'products':product,
        }

        return Response(data=data)