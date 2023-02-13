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
        self.assertEqual(data["calculated_roster"],
                        response.data["calculated_roster"]['id'])
        self.assertEqual(data["damage"], response.data["damage"])
        self.assertEqual(data["healing"], response.data["healing"])
        self.assertEqual(data["kills"], response.data["kills"])
        self.assertEqual(data["deaths"], response.data["deaths"])
        self.assertEqual(data["assists"], response.data["assists"])
        self.assertEqual(data["group"], response.data["group"])

    def test_get_calculated_roster_choice(self):
        """Get single calc roster test"""
        calculated_roster_choice = CalculatedRosterChoices.objects.first()
        response = self.client.get(
            f"/calculatedrosterchoices/{calculated_roster_choice.pk}")
        expected = CalcRostChoicesSerializer(calculated_roster_choice)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)

    def test_get_calculated_roster_choices(self):
        """Get calc rosters test"""
        url = f"/calculatedrosterchoices?calculatedroster={CalculatedRoster.objects.first().pk}"
        response = self.client.get(url)
        calculated_roster_choices = CalculatedRosterChoices.objects.filter(
            calculated_roster=CalculatedRoster.objects.first())
        expected = CalcRostChoicesSerializer(
            calculated_roster_choices, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)

    def test_get_calculated_roster_choices_no_calculated_roster(self):
        """Get calc rosters test"""
        url = f"/calculatedrosterchoices"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED,
                        response.status_code)

    def test_update_calculated_roster_choice(self):
        """Update calc roster test"""
        calculated_roster_choice = CalculatedRosterChoices.objects.first()
        url = f"/calculatedrosterchoices/{calculated_roster_choice.pk}"
        data = {
            "calculated_roster": CalculatedRoster.objects.first().pk,
            "damage": 100,
            "healing": 100,
            "kills": 100,
            "deaths": 100,
            "assists": 100,
            "group": 1
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(data["calculated_roster"],
                        response.data["calculated_roster"]['id'])
        self.assertEqual(data["damage"], response.data["damage"])
        self.assertEqual(data["healing"], response.data["healing"])
        self.assertEqual(data["kills"], response.data["kills"])
        self.assertEqual(data["deaths"], response.data["deaths"])
        self.assertEqual(data['assists'], response.data['assists'])
        # currently not accounting for character, or group number, needs to be added

    def test_delete_calculated_roster_choice(self):
        """Delete calc roster choice test"""
        calculated_roster_choice = CalculatedRosterChoices.objects.first()
        url = f"/calculatedrosterchoices/{calculated_roster_choice.pk}"
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(0, CalculatedRosterChoices.objects.filter(
            pk=calculated_roster_choice.pk).count())
