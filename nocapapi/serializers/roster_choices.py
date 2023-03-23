from rest_framework import serializers
from nocapapi.models import RosterChoices
from nocapapi.serializers.character import CharacterSerializer
from nocapapi.serializers.roster import RosterSerializer


class RostChoicesSerializer(serializers.ModelSerializer):
    """JSON serializer for roster choices serializer
    """
    character = CharacterSerializer(many=False)
    roster = RosterSerializer(many=False)
    class Meta:
        model = RosterChoices
        fields = ('id', 'character', 'roster', 'group')
        # depth = 1