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

 
    def list(self, request, pk):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        char_links = CharLink.objects.all()
        char_links = request.query_params.get('links', None)
        if char_links is not None:
            char_links = CharLink.filter(character_id=char_links)
        serializer = CharLink(char_links, many=True)
        return Response(serializer.data)

        # char_link = CharLink.objects.get(pk=pk)
        # serializer = CharLinkSerializer(char_link, many=True)
        # return Response(serializer.data)




    def create(self, request):
        """Handle POST operations"""
        # roster =
        
        character = Character.objects.get(pk=request.data['character'])
        if CalculatedRoster.objects.get(pk=request.data['roster']):
            new_link = CharLink.objects.create(
                character=character,
                link=request.data['link'],
                roster=CalculatedRoster.objects.get(pk=request.data['roster'])
                )
            serializer = CharLinkSerializer(new_link)
            return Response(serializer.data)
        else: 
            new_link = CharLink.objects.create(
            character=character,
            link=request.data['link']
            )
            serializer = CharLinkSerializer(new_link)
            return Response(serializer.data)


class CharLinkSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CharLink
        fields = ('id', 'character', 'roster', 'link')