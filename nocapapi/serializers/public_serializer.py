from rest_framework import serializers
from nocapapi.models import CalculatedRoster


# class CalculatedRosterSerializer(serializers.ModelSerializer):
#     """JSON serializer for calculated rosters
#     """
#     class Meta:
#         model = CalculatedRoster
#         fields = ('id', 'rosterName', 'roster' )

class PublicRosterListSerializer(serializers.ModelSerializer):
    """JSON serializer for calculated rosters"""
    class Meta:
        model = CalculatedRoster
        fields = ('rosterName', 'total_damage', 'total_healing', 'total_deaths', 'total_kills', 'is_public')