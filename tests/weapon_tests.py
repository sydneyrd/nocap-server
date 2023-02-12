from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from nocapapi.models import  RosterUser, Weapon
from nocapapi.views.weapon import WeaponSerializer

class WeaponTests(APITestCase):
    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'rosterusers', 'weapons' ]
    
    def setUp(self):
        # Grab the first rosteruser object from the database and add their token to the headers
        self.rosteruser = RosterUser.objects.first()
        token = Token.objects.get(user=self.rosteruser.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    def test_get_roles(self):
        """Get weapons test"""
        url = "/weapons"
        response = self.client.get(url)
        weapons = Weapon.objects.all()
        expected = WeaponSerializer(weapons, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)