from rest_framework import generics
from ..models import Category
from ..serialization import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_name']
    search_fields = ['category_name']

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_name']
    search_fields = ['category_name']