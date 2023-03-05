from django.db import IntegrityError
from rest_framework import serializers
from .models import Save


class SaveSerializer(serializers.ModelSerializer):
    """ Save Serializer """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Save
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail: possible duplicate'
            })
