from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import CalculatedRoster, RosterUser, Roster, CalculatedRosterChoices
from django.db.models import Sum, Aggregate



class CalculatedRosterView(ViewSet):
    """Level up game types view"""
    def retrieve(self, request, pk):
        try:
        # Retrieve the CalculatedRoster object
            calroster = CalculatedRoster.objects.get(pk=pk)

        # Serialize the object
            serializer = CalculatedRosterSerializer(calroster)

        # Retrieve the related CalculatedRosterChoice objects
            choices = CalculatedRosterChoices.objects.filter(calculated_roster=calroster)

        # Sum the damage, healing, kills, and deaths fields of the choices
            aggregates = choices.aggregate(
                total_damage=Sum('damage'),
                total_healing=Sum('healing'),
                total_kills=Sum('kills'),
                total_deaths=Sum('deaths')
            )

        # Update the CalculatedRoster object with the aggregated values
            calroster.total_damage = aggregates['total_damage']
            calroster.total_healing = aggregates['total_healing']
            calroster.total_kills = aggregates['total_kills']
            calroster.total_deaths = aggregates['total_deaths']

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
        roster = Roster.objects.get(pk=request.data['roster'])

        newroster = CalculatedRoster.objects.create(
            user=user,
            rosterName=request.data['rosterName'],
            roster=roster

        )
        serializer = CalculatedRosterSerializer(newroster)
        return Response(serializer.data)

    def destroy(self, request, pk):
        calculatedroster = CalculatedRoster.objects.get(pk=pk)
        calculatedroster.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CalculatedRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalculatedRoster
        fields = ('id', 'user', 'rosterName', 'roster', 'total_damage', 'total_healing', 'total_deaths', 'total_kills')
        depth = 1
