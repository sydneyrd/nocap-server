from nocapapi.models import Character
from rest_framework import serializers



class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for characters
    """
    class Meta:
        model = Character
        fields = ('id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server',  'character_name', 'user', 'notes', 'image' )


class CharacterFilterSerializer(serializers.Serializer):
    role_id = serializers.IntegerField(required=False)
    faction_id = serializers.IntegerField(required=False)
    primary_weapon_id = serializers.IntegerField(required=False)
    secondary_weapon_id = serializers.IntegerField(required=False)
    server_id = serializers.IntegerField(required=False)
    character_name = serializers.CharField(required=False)
    user_id = serializers.IntegerField(required=False)
    search_text = serializers.CharField(required=False)
