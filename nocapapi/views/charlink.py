from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import  Character, CalculatedRoster
from nocapapi.models.charlink import CharLink



class CharLinkView(ViewSet):
    """DGR Links view"""

    # def retrieve(self, request, pk):
    #     """Handle GET requests for a single 
    #     Returns:
    #         Response -- JSON serialized game type"""
    #     try:  //shouldn't need a single retrieve, just saving it cause lazy
    #         calcrostchoices = CalculatedRosterChoices.objects.get(pk=pk)
    #         serializer = CalcRostChoicesSerializer(calcrostchoices)
    #         return Response(serializer.data)
    #     except CalculatedRosterChoices.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        char_link = CharLink.objects.all()
        # calcroster = request.query_params.get('calculatedroster', None)
        # if calcroster is not None:
        #     calcrostchoices = calcrostchoices.filter(calculated_roster=calcroster)
        serializer = CharLinkSerializer(char_link, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        roster = CalculatedRoster.objects.get(pk=request.data['roster'])
        character = Character.objects.get(pk=request.data['character'])
        new_link = CharLink.objects.create(
            roster=roster,
            character=character,
            link=request.data['link'],
        )
        serializer = CharLink(new_link)
        return Response(serializer.data)



class CharLink(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CharLink
        fields = ('id', 'character', 'roster', 'link')