from rest_framework import serializers
from nocapapi.models import Server

class ServerSerializer(serializers.ModelSerializer):
    """JSON serializer for servers
    """
    class Meta:
        model = Server
        fields = ('id', 'name' )