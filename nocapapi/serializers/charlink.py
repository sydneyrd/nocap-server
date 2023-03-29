from rest_framework import serializers
from nocapapi.models import CharLink

class CharLinkSerializer(serializers.ModelSerializer):
    """JSON serializer for character links
    """
    class Meta:
        model = CharLink
        fields = ('id', 'character', 'calculated_roster', 'link')
