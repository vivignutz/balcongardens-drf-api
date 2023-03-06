from rest_framework import viewsets
from .serializers import RatingSerializer
from .models import Rating


class RatingViewSet(viewsets.ModelViewSet):
    """
    To get all plants review in random order
    """
    queryset = Rating.objects.all().order_by('?')
    serializer_class = RatingSerializer
