from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.serializers.public_serializer import PublicRosterListSerializer

class PublicTests(APITestCase):
    def test_get_public_rosters(self):
        """
        Get public rosters test"""
        url = "/public-rosters"
        response = self.client.get(url)
        expected = PublicRosterListSerializer(response.data, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)