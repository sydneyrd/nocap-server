from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from nocapapi.models import SharedCharacterToken, Character
from nocapapi.models import RosterUser
from nocapapi.serializers import CharacterSerializer
from nocapapi.serializers import CharacterReadOnlySerializer
from nocapapi.models import Role
from nocapapi.models import Weapon
from nocapapi.models import Server
from nocapapi.models import Faction
import uuid
import base64
from django.core.files.base import ContentFile
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle

# other imports you need for character creation

@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def shared_character_create(request, token):
    try:
        shared_character_token = SharedCharacterToken.objects.get(token=token)
        rosteruser = shared_character_token.user

        # Create a new character using the provided request data and associate it with the `rosteruser`
        # You can reuse/modify the existing character creation logic you have in your `create` method
        user = rosteruser
        new_role = Role.objects.get(pk=request.data["role"])
        new_primary_weapon = Weapon.objects.get(pk=request.data['primary_weapon'])
        new_secondary_weapon = Weapon.objects.get(pk=request.data['secondary_weapon'])
        new_server = Server.objects.get(pk=request.data['server'])
        new_faction = Faction.objects.get(pk=request.data['faction'])
        try:
                format, img_str = request.data["image"].split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(img_str), name=f'{request.data["character_name"]}-{uuid.uuid4()}.{ext}')
        except:
                data = None
        character = Character.objects.create(
                role=new_role,
                faction=new_faction,
                primary_weapon=new_primary_weapon,
                secondary_weapon=new_secondary_weapon,
                server=new_server,
                character_name=request.data["character_name"],
                user=user,
                image=data
            )

        return Response({"message": "Character created successfully"}, status=status.HTTP_201_CREATED)
    except SharedCharacterToken.DoesNotExist:
        return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
