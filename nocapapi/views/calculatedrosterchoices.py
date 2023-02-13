from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import CalculatedRosterChoices, Character, CalculatedRoster

class CalculatedRosterChoicesView(ViewSet):
    """Calculated Roster Choices/ the characters on rosters view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single calculated roster choice
        Returns:
            Response -- JSON serialized calculated roster choice"""
        try:
            calculated_roster_choices = CalculatedRosterChoices.objects.get(pk=pk)
            serializer = CalcRostChoicesSerializer(calculated_roster_choices)
            return Response(serializer.data)
        except CalculatedRosterChoices.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        """Handle GET requests to get all calculated roster choices
        Returns:
        Response -- JSON serialized list of calculated roster choices
    """
        try:
            calculated_roster_choices = CalculatedRosterChoices.objects.all()
            calculated_roster = request.query_params.get('calculatedroster', None)
            if calculated_roster is not None:
                calculated_roster_choices = calculated_roster_choices.filter(calculated_roster=calculated_roster)
        
            serializer = CalcRostChoicesSerializer(calculated_roster_choices, many=True)
            return Response(serializer.data)
        except CalculatedRosterChoices.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def create(self, request):
        """Handle POST operations for calculated roster choices"""
        calculated_roster = CalculatedRoster.objects.get(pk=request.data['calculated_roster'])
        character = Character.objects.get(pk=request.data['character'])
        try:
            
            if 'group' in request.data:
                group = request.data['group']
            else:
                group = 0
            new_roster_choice = CalculatedRosterChoices.objects.create(
                    calculated_roster=calculated_roster,
                    character=character,
                    damage=request.data['damage'],
                    healing=request.data['healing'],
                    kills=request.data['kills'],
                    deaths=request.data['deaths'],
                    assists=request.data['assists'],
                    group=group
            )
            serializer = CalcRostChoicesSerializer(new_roster_choice)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, pk):
        """Handle PUT requests for a calcRosterChoice
        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            calculated_roster_choice = CalculatedRosterChoices.objects.get(pk=pk)
            calculated_roster_choice.damage = request.data['damage']
            calculated_roster_choice.healing = request.data['healing']
            calculated_roster_choice.kills = request.data['kills']
            calculated_roster_choice.deaths = request.data['deaths']
            calculated_roster_choice.assists = request.data['assists']
            if 'group' in request.data:
                calculated_roster_choice.group = request.data['group']
            calculated_roster_choice.save()
            return Response({"character updated"}, status=status.HTTP_204_NO_CONTENT)
        except CalculatedRosterChoices.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def destroy(self, request, pk):
        """Handle DELETE requests for a single calculated Roster Choice
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            calculated_roster_choice = CalculatedRosterChoices.objects.get(pk=pk)
            calculated_roster_choice.delete()

            return Response({'successfully deleted from roster'}, status=status.HTTP_204_NO_CONTENT)

        except CalculatedRosterChoices.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CalculatedRosterSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CalculatedRoster
        fields = ('id', 'rosterName', 'roster' )
class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Character
        fields = ('id',
        "character_name",
        "notes",
        "image",
        "role",
        "faction",
        "primary_weapon",
        "secondary_weapon",
        "server",
        "user")
class CalcRostChoicesSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    calculated_roster = CalculatedRosterSerializer(many=False)
    character = CharacterSerializer(many=False)
    class Meta:
        model = CalculatedRosterChoices
        fields = ('id', 'character', 'calculated_roster', 'damage', 'healing', 'kills', 'deaths', 'assists', 'group'  )