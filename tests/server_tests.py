from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from nocapapi.models import  RosterUser, Server
from nocapapi.views.server import ServerSerializer

class ServerTests(APITestCase):
    def test_get_roles(self):
        """Get roles test"""
        url = "/servers"
        response = self.client.get(url)
        servers = Server.objects.all()
        expected = ServerSerializer(servers, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)