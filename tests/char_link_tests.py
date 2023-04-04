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
    def test_get_char_link_by_character(self):
        """Get character link by character test"""
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
        url = f"/links?character={Character.objects.first().pk}"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data["character"], response.data[0]["character"])
        self.assertEqual(data["calculated_roster"],
                        response.data[0]["calculated_roster"])
        self.assertEqual(data["link"], response.data[0]["link"])
    def test_delete_char_link(self):
        """Delete character link test"""
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
        url = f"/links/{CharLink.objects.first().pk}"
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(None, response.data)

    def test_get_all_char_links(self):
        """Get all character links test"""
        url = "/links"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
    

    def test_get_empty_list_no_links(self):
        """Get empty character links test"""
        character = Character.objects.last()
        url = f"/links?character={character.pk}"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([], response.data)

    

    # def test_no_matching_character_fail(self):
    #     """Get character links with no matching character test"""
    #     url = "/links?character=999999"
    #     response = self.client.get(url)
    #     self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
    #     self.assertEqual("character not found", response.data["message"])

    

    # def test_get_char_link_by_calculated_roster(self):
    #     """Get character link by calculated roster test"""
    #     url = "/links"
    #     data = {
    #         "character": Character.objects.first().pk,
    #         "calculated_roster": CalculatedRoster.objects.first().pk,
    #         "link": "https://www.google.com"
    #     }
    #     response = self.client.post(url, data, format="json")
    #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    #     self.assertEqual(data["character"], response.data["character"])
    #     self.assertEqual(data["calculated_roster"],
    #                     response.data["calculated_roster"])
    #     self.assertEqual(data["link"], response.data["link"])
    #     url = f"/links?calculated_roster={CalculatedRoster.objects.first().pk}"
    #     response = self.client.get(url)
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)
    #     self.assertEqual(data["character"], response.data[0]["character"])
    #     self.assertEqual(data["calculated_roster"],
    #                     response.data[0]["calculated_roster"])
    #     self.assertEqual(data["link"], response.data[0]["link"])

    # need to add to view