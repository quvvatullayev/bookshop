from rest_framework import generics
from ..models import Product 
from ..serialization import ProductSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = ProductSerializer
    