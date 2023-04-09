from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from nocapapi.models import CalculatedRoster, CalculatedRosterChoices, Character
from nocapapi.serializers import PublicRosterListSerializer, PublicCalcRostChoicesSerializer, CharacterReadOnlySerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def public_calculated_rosters(request):
    try:
        calculated_roster = CalculatedRoster.objects.filter(is_public=True)
        
        serializer = PublicRosterListSerializer(calculated_roster, many=True)
        return Response(serializer.data)
    except Exception as ex:
        return Response({'error': ex.args[0]})


@api_view(['GET'])
@permission_classes([AllowAny])
def public_calculated_roster_choices(request):
    try:
        calculated_roster_choices = CalculatedRosterChoices.objects.filter(calculated_roster=request.query_params.get('calculatedroster', None))
        
        serializer = PublicCalcRostChoicesSerializer(calculated_roster_choices, many=True)
        return Response(serializer.data)
    except Exception as ex:
        return Response({'error': ex.args[0]})
    
@api_view(['GET'])
@permission_classes([AllowAny])
def public_calculated_character(request, character_id):
    try:
        character = Character.objects.get(pk=character_id)
        serializer = CharacterReadOnlySerializer(character, many=False)
        return Response(serializer.data)
    except Exception as ex:
        return Response({'error': ex.args[0]})
