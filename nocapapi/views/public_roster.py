from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from nocapapi.models import CalculatedRoster
from nocapapi.serializers import PublicRosterListSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def public_calculated_rosters(request):
    calculated_roster = CalculatedRoster.objects.filter(is_public=True)
    
    serializer = PublicRosterListSerializer(calculated_roster, many=True)
    return Response(serializer.data)
