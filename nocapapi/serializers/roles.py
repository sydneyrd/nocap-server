from rest_framework import serializers
from nocapapi.models import Role

class RoleSerializer(serializers.ModelSerializer):
    """JSON serializer for roles
    """
    class Meta:
        model = Role
        fields = ('id', 'name' )