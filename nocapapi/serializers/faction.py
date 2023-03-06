from rest_framework import serializers
from nocapapi.models import Faction

class FactionSerializer(serializers.ModelSerializer):
    """JSON serializer for factions
    """
    class Meta:
        model = Faction
        fields = ('id', 'name' )