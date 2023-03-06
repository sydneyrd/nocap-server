from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from nocapapi.serializers import UserSerializer



class UserView(ViewSet):
    """User view"""
    def update(self, request, pk):
        """handle put/patch for users"""
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        # Only update the username and email fields
        user.username = request.data.get('username', user.username)
        user.email = request.data.get('email', user.email)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk):
        """Handle GET requests for single user
        Returns:
            Response -- JSON serialized user"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

# class UserSerializer(serializers.ModelSerializer):
#     """JSON serializer for users
#     """
#     class Meta:
#         model = User
#         fields = ('id', 'username' )