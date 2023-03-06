from rest_framework import serializers
from nocapapi.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for characters
    """
    class Meta:
        model = Character
        fields = ('id',
        "character_name",
        "notes",
        "image",
        "role",
        "faction",
        "primary_weapon",
        "secondary_weapon",
        "server",
        "user")