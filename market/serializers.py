from rest_framework import serializers
from .models import Plants
from saved.models import Save


class PlantsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    save_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        # se a img form maior q 2mb, da o erro
        """ Image validation for all images uploaded by users
            with error messages when larger than default
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Oh no... Your image size is lager than 2MB :-( )'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Oh no... Your image width is lager than 4096px :-( )'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Oh no... Your image height is lager than 4096px :-( )'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, plant=obj
            ).first()
            return save.id if save else None
        return None

    class Meta:
        model = Plants
        fields = [
            'image', 'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'email', 'city', 'postal_code',
            'difficulty',
        ]      # ou coloca isso pra inserir tudo: '__all__'
