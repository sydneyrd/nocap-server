from rest_framework import serializers
from nocapapi.models import CalculatedRosterChoices
from nocapapi.serializers.character import CharacterSerializer
from nocapapi.serializers.calculated_roster import CalculatedRosterSerializer
from nocapapi.serializers.charlink import CharLinkSerializer

class CalcRostChoicesSerializer(serializers.ModelSerializer):
    """JSON serializer for calcrosterchoices 
    """
    character = CharacterSerializer(many=False)
    char_links = serializers.SerializerMethodField()

    class Meta:
        model = CalculatedRosterChoices
        fields = ('id', 'character', 'damage', 'healing', 'kills', 'deaths', 'assists', 'group', 'char_links')

    def get_char_links(self, obj):
        char_links = obj.character.character_links.filter(calculated_roster=obj.calculated_roster)
        return CharLinkSerializer(char_links, many=True, read_only=True).data
