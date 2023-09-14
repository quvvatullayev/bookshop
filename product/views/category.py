from rest_framework import generics
from ..models import Category
from ..serialization import CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

