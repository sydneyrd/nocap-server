from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from nocapapi.models import SharedCalculatedRosterChoiceToken, Character, CalculatedRoster, CalculatedRosterChoices
from nocapapi.models import RosterUser
from nocapapi.serializers import CalcRostChoicesSerializer


import uuid
import base64
from django.core.files.base import ContentFile
from rest_framework.permissions import IsAuthenticated


# other imports you need for character creation

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shared_calculated_roster_choice_create(request, token):
    try:
        shared_roster_token = SharedCalculatedRosterChoiceToken.objects.get(token=token)
        calculated_roster = shared_roster_token.calculated_roster
        
        character = Character.objects.get(pk=request.data['character'])
            
        if 'group' in request.data:
                group = request.data['group']
        else:
                group = 0
        new_roster_choice = CalculatedRosterChoices.objects.create(
                    calculated_roster=calculated_roster,
                    character=character,
                    damage=request.data['damage'],
                    healing=request.data['healing'],
                    kills=request.data['kills'],
                    deaths=request.data['deaths'],
                    assists=request.data['assists'],
                    group=group
            )
        serializer = CalcRostChoicesSerializer(new_roster_choice)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
