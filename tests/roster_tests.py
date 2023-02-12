from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import Roster
from nocapapi.views.roster import RosterSerializer

class RosterTests(APITestCase):
    def test_get_roster(self):
        """Get single roster test"""
        roster = Roster.objects.first()
        response = self.client.get(f"/rosters/{roster.pk}")
        expected = RosterSerializer(roster)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_get_rosters(self):
        """Get rosters test"""
        url = "/rosters"
        response = self.client.get(url)
        rosters = Roster.objects.all()
        expected = RosterSerializer(rosters, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_create_roster(self):
        """Create roster test"""
        url = "/rosters"
        data = {
            "name": "Test Roster",
            "user": self.rosteruser.pk
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["name"], response.data["name"])
        self.assertEqual(data["user"], response.data["user"])