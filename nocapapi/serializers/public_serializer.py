from rest_framework import serializers
from nocapapi.models import CalculatedRoster
from rest_framework import serializers
from nocapapi.models import CalculatedRosterChoices
from nocapapi.serializers.character import CharacterSerializer
from nocapapi.serializers.calculated_roster import CalculatedRosterSerializer
from nocapapi.serializers.charlink import CharLinkSerializer



class PublicRosterListSerializer(serializers.ModelSerializer):
    """JSON serializer for calculated rosters"""
    class Meta:
        model = CalculatedRoster
        fields = ('rosterName', 'total_damage', 'total_healing', 'total_deaths', 'total_kills', 'is_public', 'id')


    

class PublicCalcRostChoicesSerializer(serializers.ModelSerializer):
    """JSON serializer for calcrosterchoices
    for public view 
    """
    character = CharacterSerializer(many=False)
    char_links = CharLinkSerializer(many=True, read_only=True, source='character.character_links')

    class Meta:
        model = CalculatedRosterChoices
        fields = ('id', 'character',  'damage', 'healing', 'kills', 'deaths', 'assists', 'group', 'char_links' )