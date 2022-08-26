from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import CalculatedRoster, RosterUser, Roster



class CalculatedRosterView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            calroster = CalculatedRoster.objects.get(pk=pk)
            serializer = CalculatedRosterSerializer(calroster)
            return Response(serializer.data)
        except CalculatedRoster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        calroster = CalculatedRoster.objects.all()
        user_req = request.query_params.get('user', None)
        if user_req is not None:
            calroster = calroster.filter(user=user_req)
        serializer = CalculatedRosterSerializer(calroster, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations"""
        user = RosterUser.objects.get(user_id=request.auth.user)
        if request.data['roster'] is not None:
            roster = Roster.objects.get(pk=request.data['roster'])
        else:
            roster = None
        newroster = CalculatedRoster.objects.create(
            user=user,
            rosterName=request.data['rosterName'],
            roster=roster

        )
        serializer = CalculatedRosterSerializer(newroster)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        calculatedroster = CalculatedRoster.objects.get(pk=pk)
        calculatedroster.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)




class CalculatedRosterSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CalculatedRoster
        fields = ('id', 'user', 'rosterName', 'roster'  )