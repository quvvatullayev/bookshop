from rest_framework import generics
from ..models import Like
from ..serialization import LikeSerializer

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer