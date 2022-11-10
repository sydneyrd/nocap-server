from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import  Character, CalculatedRoster
from nocapapi.models.charlink import CharLink



class CharLinkView(ViewSet):
    """DGR Links view"""

    # def retrieve(self, request, pk):
    #     """Handle GET requests for single character
    #     Returns:
    #         Response -- JSON serialized character"""
    #     try:
    #         character = CharLink.objects.get(pk=pk)
    #         serializer = CharLinkSerializer(character, many=True)
    #         return Response(serializer.data)
    #     except Character.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

 
    def list(self, request):
        """Handle GET requests to get all char_links
        Returns:
            Response -- JSON serialized list of char_links
        """
        char_links = CharLink.objects.all()
        character = request.query_params.get('character', None)
        if character is not None:
            char_links = char_links.filter(character=character)
        serializer = CharLinkSerializer(char_links, many=True)
        return Response(serializer.data)
        # char_link = CharLink.objects.get(pk=pk)
        # serializer = CharLinkSerializer(char_link, many=True)
        # return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        character = Character.objects.get(pk=request.data['character'])
        if request.data['roster'] > 0:
                new_link = CharLink.objects.create(
                    character=character,
                    link=request.data['link'],
                    calculated_roster=CalculatedRoster.objects.get(pk=request.data['roster'])
                )
        else: new_link = CharLink.objects.create(
                character=character,
                link=request.data['link'],
                )
        serializer = CharLinkSerializer(new_link)
        return Response(serializer.data)

class CharLinkSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CharLink
        fields = ('id', 'character', 'calculated_roster', 'link')