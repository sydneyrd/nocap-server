from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import Roster, RosterUser

class RosterView(ViewSet):
    """Roster view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single roster
        Returns:
            Response -- JSON serialized single roster"""
        try:
            roster = Roster.objects.get(pk=pk)
            serializer = RosterSerializer(roster)
            return Response(serializer.data)
        except Roster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        """Handle GET requests to get all rosters
    Returns:
        Response -- JSON serialized list of rosters
    """
        try:
            roster = Roster.objects.all()
            str_user = request.query_params.get('user', None)
            roster_user = RosterUser.objects.get(pk=str_user)
            if roster_user is not None:
                roster = roster.filter(user=roster_user)
                serializer = RosterSerializer(roster, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Roster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except RosterUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
    def create(self, request):
        """Handle POST operations for rosters"""
        try:
            user = RosterUser.objects.get(user_id=request.auth.user)
            if 'name' in request.data:
                new_roster = Roster.objects.create(
                    name=request.data["name"],
                    user=user
                )
            else:
                new_roster = Roster.objects.create(
                    user=user
                )
            serializer = RosterSerializer(new_roster)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, pk):
        """Handle DELETE requests for a single roster"""
        try:
            roster = Roster.objects.get(pk=pk)
            roster.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Roster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk):
        """handle put for roster"""
        try:
            roster = Roster.objects.get(pk=pk)
            roster.name = request.data["name"]
            roster.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Roster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RosterSerializer(serializers.ModelSerializer):
    """JSON serializer for  rosters
    """
    class Meta:
        model = Roster
        fields = ('id', 'user', 'name' )