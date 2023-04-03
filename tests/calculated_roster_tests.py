from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import CalculatedRoster, Roster, Character
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
    
    def test_update_calculated_roster(self):
        """Update calc roster test"""
        c = CalculatedRoster.objects.get(pk=4)
        data = {
            "id": 4,
            "rosterName": "Test Roster name change",
            "roster": 24,
            "user": 1
        }
        response = self.client.put(f"/calculatedrosters/4", data, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data['id'], response.data['id'])
        self.assertEqual(data['rosterName'], response.data['rosterName'])
        self.assertEqual(data['roster'], response.data['roster']['id'])
        self.assertEqual(data['user'], response.data['user']['id'])

    def test_delete_calculated_roster(self):
        """Delete calc roster test"""
        calculated_roster = CalculatedRoster.objects.first()
        response = self.client.delete(f"/calculatedrosters/{calculated_roster.pk}")
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({'message': "deleted"}, response.data)  
    def test_get_calculated_roster_by_character(self):
        """Get calc roster by character test"""
        url = f"/calculatedrosters?character={Character.objects.first().pk}"
        response = self.client.get(url)
        calculated_rosters = CalculatedRoster.objects.filter(calculatedrosterchoices__character=Character.objects.first().pk)
        expected = CalculatedRosterSerializer(calculated_rosters, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)  