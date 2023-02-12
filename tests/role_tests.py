from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from nocapapi.models import  RosterUser, Role
from nocapapi.views.role import RoleSerializer

class RoleTests(APITestCase):
    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'rosterusers', 'roles' ]
    
    def setUp(self):
        # Grab the first rosteruser object from the database and add their token to the headers
        self.rosteruser = RosterUser.objects.first()
        token = Token.objects.get(user=self.rosteruser.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    def test_get_roles(self):
        """Get roles test"""
        url = "/roles"
        response = self.client.get(url)
        roles = Role.objects.all()
        expected = RoleSerializer(roles, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)