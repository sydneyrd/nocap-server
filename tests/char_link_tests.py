from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import Character, CharLink, CalculatedRoster
from nocapapi.views.charlink import CharLinkSerializer


class CharLinkTests(APITestCase):
    """Character Link tests"""

    def test_create_char_link(self):
        """Create character link test"""
        url = "/links"
        data = {
            "character": Character.objects.first().pk,
            "calculated_roster": CalculatedRoster.objects.first().pk,
            "link": "https://www.google.com"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["character"], response.data["character"])
        self.assertEqual(data["calculated_roster"],
                        response.data["calculated_roster"])
        self.assertEqual(data["link"], response.data["link"])