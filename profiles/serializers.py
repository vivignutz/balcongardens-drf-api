from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.username') # nao pode ser editado
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        # aponta para o profile e especifica os campos que queremos incluir
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'content', 'image', 'is_owner'
            ]       # ou coloca isso pra inserir tudo: '__all__'
