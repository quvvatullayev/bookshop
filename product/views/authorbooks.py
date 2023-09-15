from rest_framework import generics
from ..models import AuthorBook
from ..serialization import AuthorBooksSerializer

class AuthorBooksListCreateView(generics.ListCreateAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBooksSerializer

    