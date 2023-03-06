from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """
    hfvqfjvnjvnjn
    """
    Post = serializers.ImageField
    rating = serializers.StringRelatedField(many=True)

    class Meta:
        model = Rating()
        fields = ['image', 'rating', 'content',]
