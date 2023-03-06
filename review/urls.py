from django.urls import path, include
from rest_framework import routers
from .views import RatingViewSet


router = routers.DefaultRouter()
"""
Route to receive the plants with its rating
when frontend sends it.
"""
router.register(r'posts', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('drf.api/', include(
        'rest_framework.urls', namespace='rest_framework'
        ))
]
