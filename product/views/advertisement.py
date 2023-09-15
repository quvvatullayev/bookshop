from rest_framework import generics
from ..models import Advertisement
from ..serialization import AdvertisementSerializer

class AdvertisementListCreateView(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

