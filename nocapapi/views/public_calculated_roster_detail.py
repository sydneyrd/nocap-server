from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from nocapapi.models import CalculatedRoster
from nocapapi.serializers import PublicRosterListSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def public_calculated_roster_detail(request, roster_id):
    try:
        calculated_roster = get_object_or_404(CalculatedRoster, id=roster_id, is_public=True)
        serializer = PublicRosterListSerializer(calculated_roster)
        return Response(serializer.data)
    except Exception as ex:
        return Response({'error': ex.args[0]})
