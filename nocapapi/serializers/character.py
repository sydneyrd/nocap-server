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

class CharacterReadOnlySerializer(serializers.ModelSerializer):
    """JSON serializer for characters
    with read only fields, names of foreign keys instead of fk id
    """
    role = serializers.StringRelatedField()
    faction = serializers.StringRelatedField()
    primary_weapon = serializers.StringRelatedField()
    secondary_weapon = serializers.StringRelatedField()
    server = serializers.StringRelatedField()

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
        "server")
        