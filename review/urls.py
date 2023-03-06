from django.urls import path
from .views import RatingView

urlpatterns = [
    path('review/', RatingView.as_view(), name='review'),
    path('review/<int:pk>/', RatingView.as_view()),
]
