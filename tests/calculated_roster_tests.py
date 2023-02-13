from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import CalculatedRoster, Roster
from nocapapi.views.calculatedroster import CalculatedRosterSerializer

class CalculatedRosterTests(APITestCase):
    """Calculated Roster tests"""
    def test_create_calculated_roster(self):
        """Create calc roster test"""
        url = "/calculatedrosters"
        data = {
            "rosterName": "Test Roster",
            "roster": Roster.objects.first().pk,    
            "user": self.rosteruser.pk
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["rosterName"], response.data["rosterName"])
        self.assertEqual(data["user"], response.data["user"]["id"])
        self.assertEqual(data["roster"], response.data["roster"]['id'])
    def test_get_calculated_roster(self):
        """Get single calc roster test"""
        calculated_roster = CalculatedRoster.objects.first()
        response = self.client.get(f"/calculatedrosters/{calculated_roster.pk}")
        expected = CalculatedRosterSerializer(calculated_roster)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_get_calculated_rosters(self):
        """Get calc rosters test"""
        url = f"/calculatedrosters?user={self.rosteruser.pk}"
        response = self.client.get(url)
        calculated_rosters = CalculatedRoster.objects.filter(user=self.rosteruser)
        expected = CalculatedRosterSerializer(calculated_rosters, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    
    def test_create_calculated_roster_no_name(self):
        """Create calc roster no name test"""
        url = "/calculatedrosters"
        data = {
            "roster": Roster.objects.first().pk,    
            "user": self.rosteruser.pk
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["user"], response.data["user"]["id"])
        self.assertEqual(data["roster"], response.data["roster"]['id'])         
    def test_create_calculated_roster_no_roster(self):  
        """Create calc roster no roster test"""
        url = "/calculatedrosters"
        data = {
            "rosterName": "Test Roster",
            "user": self.rosteruser.pk
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["user"], response.data["user"]["id"])
        self.assertEqual(data["rosterName"], response.data["rosterName"])     