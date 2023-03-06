from rest_framework import serializers, generics
from .models import Rating
from .serializers import RatingSerializer


class RatingView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
