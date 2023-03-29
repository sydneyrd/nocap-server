from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from nocapapi.models import Server
from nocapapi.serializers import ServerSerializer



class ServerView(ViewSet):
    """server view"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single server
        Returns:
            Response -- JSON serialized server instance"""
        try:
            server = Server.objects.get(pk=pk)
            serializer = ServerSerializer(server)
            return Response(serializer.data)
        except Server.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all servers
        Returns:
            Response -- JSON serialized list of servers
        """
        try:
            server = Server.objects.all()
            serializer = ServerSerializer(server, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)



# class ServerSerializer(serializers.ModelSerializer):
#     """JSON serializer for servers
#     """
#     class Meta:
#         model = Server
#         fields = ('id', 'name' )