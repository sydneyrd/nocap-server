from rest_framework import serializers
from nocapapi.models import CalculatedRosterChoices
from nocapapi.serializers.character import CharacterSerializer
from nocapapi.serializers.calculated_roster import CalculatedRosterSerializer
from nocapapi.serializers.charlink import CharLinkSerializer

class CalcRostChoicesSerializer(serializers.ModelSerializer):
    """JSON serializer for calcrosterchoices 
    """
    # calculated_roster = CalculatedRosterSerializer(many=False)
    character = CharacterSerializer(many=False)
    char_links = CharLinkSerializer(many=True, read_only=True, source='character.character_links')

    # i need to any charlinks that are associated with this calculatedroster via the character and then the calculated roster also

    

    class Meta:
        model = CalculatedRosterChoices
        fields = ('id', 'character',  'damage', 'healing', 'kills', 'deaths', 'assists', 'group', 'char_links' )