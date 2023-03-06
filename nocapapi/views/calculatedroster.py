from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from nocapapi.models import CalculatedRoster, RosterUser, Roster, CalculatedRosterChoices
from nocapapi.serializers import  CalculatedRosterSerializer


class CalculatedRosterView(ViewSet):
    """calculated roster view"""
    def retrieve(self, request, pk):
        try:
            calculated_roster = CalculatedRoster.objects.get(pk=pk)
            serializer = CalculatedRosterSerializer(calculated_roster)
            return Response(serializer.data)
        except CalculatedRoster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to get all calculated rosters
        Returns:
            Response -- JSON serialized list of calculated rosters
        """
        calculated_roster = CalculatedRoster.objects.all()
        user_req = request.query_params.get('user', None)
        if user_req is not None:
            calculated_roster = calculated_roster.filter(user=user_req)
        serializer = CalculatedRosterSerializer(calculated_roster, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for calculated rosters"""
        user = RosterUser.objects.get(user_id=request.auth.user)
        try:
            roster = Roster.objects.get(pk=request.data['roster'])
        except: 
            roster = None
        try:
            name = request.data['rosterName']
        except:
            name = None    
        try:
            new_roster = CalculatedRoster.objects.create(
                user=user,
                rosterName=name,
                roster=roster
            )
            serializer = CalculatedRosterSerializer(new_roster)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def update(self, request, pk):
        """Handle PUT requests for a calculated roster
        Returns: the serialized calculated roster, and status 200
        """
        try:
            roster = CalculatedRoster.objects.get(pk=pk)
            if request.data["rosterName"] is not None:
                roster.rosterName = request.data["rosterName"]
            if request.data["roster"] is not None:
                roster.roster = Roster.objects.get(pk=request.data["roster"])
            roster.save()
            serializer = CalculatedRosterSerializer(roster)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Roster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk):
        """Handle DELETE requests for a single calculated roster"""
        try:
            calculated_roster = CalculatedRoster.objects.get(pk=pk)
            calculated_roster.delete()
            return Response({'message': "deleted"}, status=status.HTTP_204_NO_CONTENT)
        except CalculatedRoster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

