from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class UserView(ViewSet):
    """User view"""
    def update(self, request, pk):
        """handle put for users"""
        current_user = User.objects.get(pk=request.data['id'])
        current_user.email = request.data["email"]
        current_user.first_name = request.data['first_name']
        current_user.last_name = request.data['last_name']
        current_user.username = request.data['username']
        current_user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

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

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username', 'last_name',  'email', 'is_staff', 'is_active', 'date_joined', 'first_name' )