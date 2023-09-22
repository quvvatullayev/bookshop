from rest_framework import generics
from ..models import Advertisement
from ..serialization import AdvertisementSerializer 
from ..models import Product
from ..serialization import ProductSerializer
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from user.views.authuser import ReadOnly

class AdvertisementListCreateView(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAdminUser|ReadOnly]

class AdvertisementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    
    def retrieve(self, request, *args, **kwargs):
        advertisement_obj = Advertisement.objects.get(id = kwargs['pk'])
        advertisement = AdvertisementSerializer(advertisement_obj, many = False).data

        product_obj = Product.objects.get(id = advertisement['product'])
        product = ProductSerializer(product_obj, many = False).data

        return Response(reverse_lazy(request=request, viewname='category:product', kwargs={'pk':product['id']}))