from rest_framework import serializers
from nocapapi.models import CalculatedRoster
from nocapapi.serializers.roster import RosterSerializer
from nocapapi.serializers.user import RosterUserSerializer

class CalculatedRosterSerializer(serializers.ModelSerializer):
    """JSON serializer for calculated rosters"""
    roster = RosterSerializer(many=False)
    class Meta:
        model = CalculatedRoster
        fields = ('id',  'rosterName', 'roster', 'total_damage', 'total_healing', 'total_deaths', 'total_kills', 'is_public', 'created_at', 'server' )