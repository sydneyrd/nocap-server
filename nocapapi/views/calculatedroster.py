from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import CalculatedRoster, RosterUser, Roster, CalculatedRosterChoices
from django.db import connection


class CalculatedRosterView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        try:
            calroster = CalculatedRoster.objects.get(pk=pk)
            serializer = CalculatedRosterSerializer(calroster)

        # Obtain a database cursor
            cursor = connection.cursor()

        # Execute the SELECT statement and fetch the results
            cursor.execute("""
            SELECT SUM(nocapapi_calculatedrosterchoices.damage) AS total_damage,
                   SUM(nocapapi_calculatedrosterchoices.healing) AS total_healing,
                   SUM(nocapapi_calculatedrosterchoices.kills) AS total_kills,
                   SUM(nocapapi_calculatedrosterchoices.deaths) AS total_deaths
            FROM nocapapi_calculatedroster
            JOIN nocapapi_calculatedrosterchoices
              ON nocapapi_calculatedroster.id = nocapapi_calculatedrosterchoices.calculated_roster_id
            WHERE nocapapi_calculatedroster.id = %s
        """, (pk,))
            row = cursor.fetchone()
            calroster.total_damage = row[0]
            calroster.total_healing = row[1]
            calroster.total_kills = row[2]
            calroster.total_deaths = row[3]
            calroster.save()

            return Response(serializer.data)
        except CalculatedRoster.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    # def retrieve(self, request, pk):
    #     """Handle GET requests for single war result roster type
    #     Returns:
    #         Response -- JSON serialized roster results"""
    #     try:
    #         calroster = CalculatedRoster.objects.get(pk=pk)
    #         serializer = CalculatedRosterSerializer(calroster)
    #         return Response(serializer.data)
    #     except CalculatedRoster.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    # def retrieve(self, request, pk):
    #     try:
    #         calroster = CalculatedRoster.objects.get(pk=pk)
    #         serializer = CalculatedRosterSerializer(calroster)

    #     # Execute the SELECT statement and return the results as a tuple of dictionaries
    #         results = RawSQL("""
    #         SELECT SUM(nocapapi_calculatedrosterchoices.damage) AS army_damage,
    #                SUM(nocapapi_calculatedrosterchoices.healing) AS army_healing,
    #                SUM(nocapapi_calculatedrosterchoices.kills) AS army_kills,
    #                SUM(nocapapi_calculatedrosterchoices.deaths) AS army_deaths
    #         FROM calculated_roster
    #         JOIN nocapapi_calculatedrosterchoices
    #           ON calculated_roster.id = nocapapi_calculatedrosterchoices.calculated_roster_id
    #         WHERE calculated_roster.id = %s
    #     """, (pk,))

    #     # Add the results to the serializer data
    #         serializer.data['results'] = results

    #         return Response(serializer.data)
    #     except CalculatedRoster.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

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
