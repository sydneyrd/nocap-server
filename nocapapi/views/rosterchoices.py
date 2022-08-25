from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import RosterChoices, Roster, Character



class RosterChoicesView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            rostchoices = RosterChoices.objects.get(pk=pk)
            serializer = RostChoicesSerializer(rostchoices)
            return Response(serializer.data)
        except RosterChoices.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        rostchoices = RosterChoices.objects.all()
        roster_id = request.query_params.get('roster', None)
        if roster_id is not None:
            rostchoices = rostchoices.filter(roster=roster_id)
        serializer = RostChoicesSerializer(rostchoices, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        roster = Roster.objects.get(pk=request.data['roster'])
        character = Character.objects.get(pk=request.data['character'])
        newrosterchoice = RosterChoices.objects.create(
            roster=roster,
            character=character
        )
        serializer = RostChoicesSerializer(newrosterchoice)
        return Response(serializer.data)
        
    def destroy(self, request, pk):
        rosterchoice = RosterChoices.objects.get(pk=pk)
        rosterchoice.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RostChoicesSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = RosterChoices
        fields = ('id', 'character', 'roster')