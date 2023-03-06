from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nocapapi.models import Role
from nocapapi.serializers import RoleSerializer


class RoleView(ViewSet):
    """role view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single role
        Returns:
            Response -- JSON serialized role"""
        try:
            role = Role.objects.get(pk=pk)
            serializer = RoleSerializer(role)
            return Response(serializer.data)
        except Role.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    def list(self, request):
        """Handle GET requests to get all roles
        Returns:
            Response -- JSON serialized list of roles
        """
        try:
            role = Role.objects.all()
            serializer = RoleSerializer(role, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


# class RoleSerializer(serializers.ModelSerializer):
#     """JSON serializer for roles
#     """
#     class Meta:
#         model = Role
#         fields = ('id', 'name' )