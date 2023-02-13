from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import RosterChoices, Roster, Character 
from nocapapi.views.rosterchoices import RostChoicesSerializer

class RosterChoicesTests(APITestCase):
    """ Roster choices tests"""

    def test_create_calculated_roster_choice(self):
        """Create a roster choice test"""
        url = "/rosterchoices"
        data = {
            "character": Character.objects.first().pk,
            "roster": Roster.objects.first().pk
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["character"], response.data["character"])
        self.assertEqual(data["roster"],
                        response.data["roster"])
    def test_get_roster_choices_by_roster(self):
        """Get roster choices by roster test"""
        choices = RosterChoices.objects.filter(roster=Roster.objects.first())
        expected = RostChoicesSerializer(choices, many=True)
        url = f"/rosterchoices?roster={Roster.objects.first().pk}"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_get_single_roster_choice(self):
        """Get single roster choice test"""
        choice = RosterChoices.objects.first()
        expected = RostChoicesSerializer(choice)
        url = f"/rosterchoices/{choice.pk}"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_delete_roster_choice(self):
        """Delete a roster choice test"""
        choice = RosterChoices.objects.first()
        url = f"/rosterchoices/{choice.pk}"
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(None, response.data)
    