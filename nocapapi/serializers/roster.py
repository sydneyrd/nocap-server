from nocapapi.models import Roster
from rest_framework import serializers

class RosterSerializer(serializers.ModelSerializer):
    """JSON serializer for  rosters
    """
    class Meta:
        model = Roster
        fields = ('id', 'user', 'name' )