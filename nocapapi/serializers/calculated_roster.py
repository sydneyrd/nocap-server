from rest_framework import serializers
from nocapapi.models import CalculatedRoster
from nocapapi.serializers.roster import RosterSerializer
from nocapapi.serializers.user import RosterUserSerializer

# class CalculatedRosterSerializer(serializers.ModelSerializer):
#     """JSON serializer for calculated rosters
#     """
#     class Meta:
#         model = CalculatedRoster
#         fields = ('id', 'rosterName', 'roster' )

class CalculatedRosterSerializer(serializers.ModelSerializer):
    """JSON serializer for calculated rosters"""
    roster = RosterSerializer(many=False)
    user = RosterUserSerializer(many=False)
    class Meta:
        model = CalculatedRoster
        fields = ('id', 'user', 'rosterName', 'roster', 'total_damage', 'total_healing', 'total_deaths', 'total_kills', )