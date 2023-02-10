from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import CalculatedRosterChoices, Character, CalculatedRoster
from django.db.models import Sum, Aggregate



class CalculatedRosterChoicesView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            calcrostchoices = CalculatedRosterChoices.objects.get(pk=pk)
            serializer = CalcRostChoicesSerializer(calcrostchoices)
            return Response(serializer.data)
        except CalculatedRosterChoices.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
        Response -- JSON serialized list of game types
    """
        calcrostchoices = CalculatedRosterChoices.objects.all()
        calcroster = request.query_params.get('calculatedroster', None)
        if calcroster is not None:
            calcrostchoices = calcrostchoices.filter(calculated_roster=calcroster)
    
        serializer = CalcRostChoicesSerializer(calcrostchoices, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        """Handle POST operations"""
        calculatedroster = CalculatedRoster.objects.get(pk=request.data['calculated_roster'])
        character = Character.objects.get(pk=request.data['character'])

        if request.data['group'] != 0:
            newrosterchoice = CalculatedRosterChoices.objects.create(
                calculated_roster=calculatedroster,
                character=character,
                damage=request.data['damage'],
                healing=request.data['healing'],
                kills=request.data['kills'],
                deaths=request.data['deaths'],
                assists=request.data['assists'],
                group=request.data['group']
        )
        else:
            newrosterchoice=CalculatedRosterChoices.objects.create(
                    calculated_roster=calculatedroster,
                    character=character,
                    damage=request.data['damage'],
                    healing=request.data['healing'],
                    kills=request.data['kills'],
                    deaths=request.data['deaths'],
                    assists=request.data['assists']
            )

        serializer = CalcRostChoicesSerializer(newrosterchoice)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a calcRosterChoice
        Returns:
            Response -- Empty body with 204 status code
        """
        calcrostchoices = CalculatedRosterChoices.objects.get(pk=pk)
        calcrostchoices.damage = request.data['damage']
        calcrostchoices.healing = request.data['healing']
        calcrostchoices.kills = request.data['kills']
        calcrostchoices.deaths = request.data['deaths']
        calcrostchoices.assists = request.data['assists']
        if 'group' in request.data:
            calcrostchoices.group = request.data['group']
        calcrostchoices.save()

        return Response({"character updated"}, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        """Handle DELETE requests for a single calcRosterChoice
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            calcrostchoices = CalculatedRosterChoices.objects.get(pk=pk)
            calcrostchoices.delete()

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