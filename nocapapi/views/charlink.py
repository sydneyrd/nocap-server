from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import Character, CalculatedRoster
from nocapapi.models.charlink import CharLink
from nocapapi.serializers.charlink import CharLinkSerializer

class CharLinkView(ViewSet):
    """character links view"""

    def list(self, request):
        """Handle GET requests to get all char_links
        Returns:
            Response -- JSON serialized list of char_links
        """
        char_links = CharLink.objects.all()
        character = request.query_params.get('character', None)
        try:
            
            if character is not None:
                char_links = char_links.filter(character=character)
                serializer = CharLinkSerializer(char_links, many=True)
                return Response(serializer.data)
            else:
                return Response({'message': "failed"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        """Handle POST operations for character links"""
        try:
            character = Character.objects.get(pk=request.data['character'])
            if 'calculated_roster' in request.data:
                new_link = CharLink.objects.create(
                    character=character,
                    link=request.data['link'],
                    calculated_roster=CalculatedRoster.objects.get(
                        pk=request.data['calculated_roster'])
                )
            else:
                new_link = CharLink.objects.create(
                    character=character,
                    link=request.data['link'],
                )
            serializer = CharLinkSerializer(new_link)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({'message': "failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk):
        """Handle DELETE requests for a single character link"""
        try:
            link = CharLink.objects.get(pk=pk)
            link.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except CharLink.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class CharLinkSerializer(serializers.ModelSerializer):
#     """JSON serializer for character links
#     """
#     class Meta:
#         model = CharLink
#         fields = ('id', 'character', 'calculated_roster', 'link')
