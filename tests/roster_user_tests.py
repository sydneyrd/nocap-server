from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import RosterUser
from nocapapi.views.rosteruser import RosterUserSerializer

class RosterUserTests(APITestCase):
    """Roster user tests"""
    def test_get_roster_user(self):
        """Get single roster test"""
        roster_user = RosterUser.objects.first()
        response = self.client.get(f"/rosterusers/{roster_user.pk}")
        expected = RosterUserSerializer(roster_user)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    