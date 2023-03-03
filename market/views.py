from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import PlantsList
from .serializers import PostSerializer


class PlantsList(generics.ListCreateAPIView):
    """
    List of all plants to exchange or create an offer if logged in.
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PlantsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'comments_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlantsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    Update or delete a posting for owner of the post.
    """
    serializer_class = PlantsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plants.objects.all()

