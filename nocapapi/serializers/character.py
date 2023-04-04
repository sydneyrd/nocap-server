from rest_framework import serializers
from nocapapi.models import Character
from nocapapi.serializers.charlink import CharLinkSerializer


class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for characters
    """
    character_links=CharLinkSerializer(many=True, read_only=True)
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
        "character_links")

class CharacterReadOnlySerializer(serializers.ModelSerializer):
    """JSON serializer for characters
    with read only fields, names of foreign keys instead of fk id
    """
    role = serializers.StringRelatedField()
    faction = serializers.StringRelatedField()
    primary_weapon = serializers.StringRelatedField()
    secondary_weapon = serializers.StringRelatedField()
    server = serializers.StringRelatedField()
    character_links=CharLinkSerializer(many=True, read_only=True)
    

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
        "character_links")
        