from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class UserView(ViewSet):
    """Level up game types view"""


    def update(self, request, pk):
        """handle put"""

        currentuser = User.objects.get(pk=request.data['id'])
        currentuser.email = request.data["email"]
        currentuser.first_name = request.data['first_name']
        currentuser.last_name = request.data['last_name']
        currentuser.username = request.data['username']
        currentuser.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username', 'last_name',  'email', 'is_staff', 'is_active', 'date_joined', 'first_name' )