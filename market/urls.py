from django.urls import path
from cars import views

urlpatterns = [
    path('plants/', views.Plants().as_view()),
    path('plants/<int:pk>/', views.PlantsDetails().as_view()),
]