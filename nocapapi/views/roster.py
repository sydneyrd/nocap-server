from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import Roster, RosterUser



class RosterView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            roster = Roster.objects.get(pk=pk)
            serializer = RosterSerializer(roster)
            return Response(serializer.data)
        except Roster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        roster = Roster.objects.all()
        roster_user = request.query_params.get('user', None)
        if roster_user is not None:
            roster = roster.filter(user=roster_user)
        serializer = RosterSerializer(roster, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations"""
        user = RosterUser.objects.get(user_id=request.auth.user)
        
        newroster = Roster.objects.create(
            user=user
        )
        serializer = RosterSerializer(newroster)
        return Response(serializer.data)
        
    def destroy(self, request, pk):
        roster = Roster.objects.get(pk=pk)
        roster.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class RosterSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Roster
        fields = ('id', 'user' )