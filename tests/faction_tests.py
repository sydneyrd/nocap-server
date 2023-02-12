from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import  Faction
from nocapapi.views.faction import FactionSerializer

class FactionTests(APITestCase):
    def test_get_roles(self):
        """Get roles test"""
        url = "/factions"
        response = self.client.get(url)
        factions = Faction.objects.all()
        expected = FactionSerializer(factions, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)