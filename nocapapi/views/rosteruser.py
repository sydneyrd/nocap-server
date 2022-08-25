from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import RosterUser



class RosterUserView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            rosteruser = RosterUser.objects.get(pk=pk)
            serializer = RosterUserSerializer(rosteruser)
            return Response(serializer.data)
        except RosterUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        rosteruser = RosterUser.objects.all()
        # game_type = request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type_id=game_type)
        serializer = RosterUserSerializer(rosteruser, many=True)
        return Response(serializer.data)



class RosterUserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = RosterUser
        fields = ('id', 'user' )