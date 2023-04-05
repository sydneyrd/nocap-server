from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from nocapapi.models import Faction, Weapon, Role, Server
from nocapapi.serializers import FactionSerializer, WeaponSerializer, ServerSerializer, RoleSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def public_factions(request):
    try:
        factions = Faction.objects.all()
        
        serializer = FactionSerializer(factions, many=True)
        return Response(serializer.data)
    except Exception as ex:
        return Response({'error': ex.args[0]})


@api_view(['GET'])
@permission_classes([AllowAny])
def public_weapons(request):
    try:
        weapons = Weapon.objects.all()
        
        serializer = WeaponSerializer(weapons, many=True)
        return Response(serializer.data)
    except Exception as ex:
        return Response({'error': ex.args[0]})

@api_view(['GET'])
@permission_classes([AllowAny])
def public_servers(request):
    try:
        servers = Server.objects.all()
        
        serializer = ServerSerializer(servers, many=True)
        return Response(serializer.data)
    except Exception as ex:
        return Response({'error': ex.args[0]})

@api_view(['GET'])
@permission_classes([AllowAny])
def public_roles(request):
    try:
        roles = Role.objects.all()
        
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)
    except Exception as ex:
        return Response({'error': ex.args[0]})

