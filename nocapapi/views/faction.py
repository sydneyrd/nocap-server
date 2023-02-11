from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import Faction



class FactionView(ViewSet):
    """faction view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single faction
            Response -- JSON serialized faction"""
        try:
            faction = Faction.objects.get(pk=pk)
            serializer = FactionSerializer(faction)
            return Response(serializer.data)
        except Faction.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all factions
        Returns:
            Response -- JSON serialized list of factions
        """
        try:
            faction = Faction.objects.all()
            serializer = FactionSerializer(faction, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)



class FactionSerializer(serializers.ModelSerializer):
    """JSON serializer for factions
    """
    class Meta:
        model = Faction
        fields = ('id', 'name' )