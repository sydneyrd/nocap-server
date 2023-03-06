from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import Weapon
from nocapapi.serializers import WeaponSerializer

class WeaponView(ViewSet):
    """weapon view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single weapon
        Returns:
            Response -- JSON serialized weapon"""
        try:
            weapon = Weapon.objects.get(pk=pk)
            serializer = WeaponSerializer(weapon)
            return Response(serializer.data)
        except Weapon.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all weapons
        Returns:
            Response -- JSON serialized list of weapons
        """
        try:
            weapon = Weapon.objects.all()
            serializer = WeaponSerializer(weapon, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

# class WeaponSerializer(serializers.ModelSerializer):
#     """JSON serializer for weapons
#     """
#     class Meta:
#         model = Weapon
#         fields = ('id', 'name' )