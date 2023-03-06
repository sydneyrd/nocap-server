from rest_framework import serializers
from nocapapi.models import Weapon

class WeaponSerializer(serializers.ModelSerializer):
    """JSON serializer for weapons
    """
    class Meta:
        model = Weapon
        fields = ('id', 'name' )