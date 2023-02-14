from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import Character
from nocapapi.models import RosterUser, Weapon, Role, Faction, Server
import uuid
import base64
from django.core.files.base import ContentFile


class CharacterView(ViewSet):
    """Character  view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single character
        Returns:
            Response -- JSON serialized character"""
        try:
            character = Character.objects.get(pk=pk)
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        except Character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def list(self, request):
        """Handle GET requests to get all characters
        Returns:
            Response -- JSON serialized list of characters
        """
        try:
            characters = Character.objects.all()
            user_char = request.query_params.get('user', None)
            if user_char is not None:
                characters = characters.filter(user_id=user_char)
            serializer = CharacterSerializer(characters, many=True)
            return Response(serializer.data)
        except Character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        """Handle POST operations for characters"""
        try:
            user = RosterUser.objects.get(user_id=request.auth.user)
            new_role = Role.objects.get(pk=request.data["role"])
            new_primary_weapon = Weapon.objects.get(pk=request.data['primary_weapon'])
            new_secondary_weapon = Weapon.objects.get(pk=request.data['secondary_weapon'])
            new_server = Server.objects.get(pk=request.data['server'])
            new_faction = Faction.objects.get(pk=request.data['faction'])
            if 'image' in request.data:
                format, img_str = request.data["image"].split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(img_str), name=f'{request.data["character_name"]}-{uuid.uuid4()}.{ext}')
            else:
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
            serializer = CharacterSerializer(character)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        """handle put for characters"""
        try:
            character = Character.objects.get(pk=pk)
            character.role = Role.objects.get(pk=request.data["role"])
            character.faction = Faction.objects.get(pk=request.data["faction"])
            character.primary_weapon = Weapon.objects.get(pk=request.data["primary_weapon"])
            character.secondary_weapon = Weapon.objects.get(pk=request.data["secondary_weapon"])
            character.server = Server.objects.get(pk=request.data["server"])
            character.character_name = request.data["character_name"]
            if 'image' in request.data:

                if request.data["image"].startswith('data'):
                    format, imgstr = request.data["image"].split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["character_name"]}-{uuid.uuid4()}.{ext}')
                else:
                    data = None
            else:
                character.image = None
            if 'notes' in request.data:
                character.notes = request.data['notes']
            else:
                character.notes = None
            character.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk):
        """Handle DELETE requests for a single character"""
        try:
            character = Character.objects.get(pk=pk)
            character.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Character.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for characters
    """
    class Meta:
        model = Character
        fields = ('id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server',  'character_name', 'user', 'notes', 'image' )