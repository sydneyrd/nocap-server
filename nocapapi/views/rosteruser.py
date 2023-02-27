from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import RosterUser
from django.contrib.auth.models import User


class RosterUserView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for roster user
        Returns:
            Response -- JSON serialized roster user"""
        try:
            roster_user = RosterUser.objects.get(pk=pk)
            serializer = RosterUserSerializer(roster_user)
            return Response(serializer.data)
        except RosterUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        """Handle GET requests to get all roster user
        Returns:
            Response -- JSON serialized list of roster user
        """
        try:
            roster_user = RosterUser.objects.all()
            serializer = RosterUserSerializer(roster_user, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    class Meta:
        model = User
        fields = ('username', 'email')
class RosterUserSerializer(serializers.ModelSerializer):
    """JSON serializer for roster users
    """
    user = UserSerializer(many=False)
    class Meta:
        model = RosterUser
        fields = ('id', 'user' )