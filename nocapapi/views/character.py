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
    """Level up game types view"""

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
        

    def list(self, request):
        """Handle GET requests to get all characters
        Returns:
            Response -- JSON serialized list of characters
        """
        characters = Character.objects.all()
        user_char = request.query_params.get('user', None)
        if user_char is not None:
            characters = characters.filter(user_id=user_char)
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        user = RosterUser.objects.get(user_id=request.auth.user)
        newrole = Role.objects.get(pk=request.data["role"])
        newprimary_weapon = Weapon.objects.get(pk=request.data['primary_weapon'])
        newsecondary_weapon = Weapon.objects.get(pk=request.data['secondary_weapon'])
        newserver = Server.objects.get(pk=request.data['server'])
        newfaction = Faction.objects.get(pk=request.data['faction'])
        format, imgstr = request.data["image"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["character_name"]}-{uuid.uuid4()}.{ext}')
        character = Character.objects.create(
            role=newrole,
            faction=newfaction,
            primary_weapon=newprimary_weapon,
            secondary_weapon=newsecondary_weapon,
            server=newserver,
            character_name=request.data["character_name"],
            user=user,
            image=data
        )
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def update(self, request, pk):
        """handle put"""
        character = Character.objects.get(pk=pk)
        character.role = Role.objects.get(pk=request.data["role"])
        character.faction = Faction.objects.get(pk=request.data["faction"])
        character.primary_weapon = Weapon.objects.get(pk=request.data["primary_weapon"])
        character.secondary_weapon = Weapon.objects.get(pk=request.data["secondary_weapon"])
        character.server = Server.objects.get(pk=request.data["server"])
        character.character_name = request.data["character_name"]
        character.notes = request.data['notes']
        if request.data["image"].startswith('data'):

            format, imgstr = request.data["image"].split(';base64,')
            ext = format.split('/')[-1]
            
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["character_name"]}-{uuid.uuid4()}.{ext}')
        else:
            data = character.image
        character.image=data

        character.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        character = Character.objects.get(pk=pk)
        character.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class CharacterSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Character
        fields = ('id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server',  'character_name', 'user', 'notes', 'image' )
        
        