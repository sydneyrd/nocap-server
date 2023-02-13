from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import CalculatedRosterChoices, Roster, Character, CalculatedRoster
from nocapapi.views.calculatedrosterchoices import CalcRostChoicesSerializer

class CalculatedRosterChoicesTests(APITestCase):
    """Calculated Roster tests"""
    def test_create_calculated_roster_choice(self):
        """Create calc roster test"""
        url = "/calculatedrosterchoices"
        data = {
            "character": Character.objects.first().pk,
            "calculated_roster": CalculatedRoster.objects.first().pk,    
            "damage": 100,
    "healing": 100, 
    "kills": 100, 
    "deaths": 100,
    "assists": 100, 
    "group": 1 

        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["character"], response.data["character"]['id'])
        self.assertEqual(data["calculated_roster"], response.data["calculated_roster"]['id'])
        self.assertEqual(data["damage"], response.data["damage"])
        self.assertEqual(data["healing"], response.data["healing"])
        self.assertEqual(data["kills"], response.data["kills"])
        self.assertEqual(data["deaths"], response.data["deaths"])
        self.assertEqual(data["assists"], response.data["assists"])
        self.assertEqual(data["group"], response.data["group"])