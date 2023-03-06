from rest_framework import serializers
from nocapapi.models import CalculatedRosterChoices
from nocapapi.serializers.character import CharacterSerializer
from nocapapi.serializers.calculated_roster import CalculatedRosterSerializer

class CalcRostChoicesSerializer(serializers.ModelSerializer):
    """JSON serializer for calcrosterchoices 
    """
    calculated_roster = CalculatedRosterSerializer(many=False)
    character = CharacterSerializer(many=False)
    class Meta:
        model = CalculatedRosterChoices
        fields = ('id', 'character', 'calculated_roster', 'damage', 'healing', 'kills', 'deaths', 'assists', 'group'  )