from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import RosterChoices, Roster, Character
from nocapapi.serializers import RostChoicesSerializer

class RosterChoicesView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single roster choice
        Returns:
            Response -- JSON serialized roster choice"""
        try:
            roster_choices = RosterChoices.objects.get(pk=pk)
            serializer = RostChoicesSerializer(roster_choices)
            return Response(serializer.data)
        except RosterChoices.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all roster choices
        Returns:
            Response -- JSON serialized list of roster choices
        """
        try:
            roster_choices = RosterChoices.objects.all()
            roster_id = request.query_params.get('roster', None)
            if roster_id is not None:
                roster_choices = roster_choices.filter(roster=roster_id)
                serializer = RostChoicesSerializer(roster_choices, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def create(self, request):
        """Handle POST operations for roster choices
        Response -- JSON serialized roster choice instance"""
        try:
            roster = Roster.objects.get(pk=request.data['roster'])
            character = Character.objects.get(pk=request.data['character'])
            newrosterchoice = RosterChoices.objects.create(
                roster=roster,
                character=character
            )
            serializer = RostChoicesSerializer(newrosterchoice)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk):
        """Handle DELETE requests for a single roster choice"""
        try:
            roster_choice = RosterChoices.objects.get(pk=pk)
            roster_choice.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except RosterChoices.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


# class RostChoicesSerializer(serializers.ModelSerializer):
#     """JSON serializer for roster choices serializer
#     """
#     class Meta:
#         model = RosterChoices
#         fields = ('id', 'character', 'roster')
#         depth = 1