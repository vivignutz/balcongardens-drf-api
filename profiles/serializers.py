from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.username')
    # nao pode ser editado

    class Meta:
        # aponta para o profile e especifica os campos que queremos incluir
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'content', 'image'
            ]       # ou coloca isso pra inserir tudo: '__all__'
