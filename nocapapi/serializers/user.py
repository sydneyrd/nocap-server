from rest_framework import serializers
from nocapapi.models import RosterUser
from django.contrib.auth.models import User


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