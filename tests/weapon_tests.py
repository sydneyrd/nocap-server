from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import Weapon
from nocapapi.views.weapon import WeaponSerializer

class WeaponTests(APITestCase):
    def test_get_roles(self):
        """Get weapons test"""
        url = "/weapons"
        response = self.client.get(url)
        weapons = Weapon.objects.all()
        expected = WeaponSerializer(weapons, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)