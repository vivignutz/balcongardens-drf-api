from rest_framework import generics, permissions
from .models import Save
from .serializers import SaveSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class SaveList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SaveDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()
