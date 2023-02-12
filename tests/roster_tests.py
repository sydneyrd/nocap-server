from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import Roster
from nocapapi.views.roster import RosterSerializer


class RosterTests(APITestCase):
    
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
    def test_get_roster(self):
        """Get single roster test"""
        roster = Roster.objects.first()
        response = self.client.get(f"/rosters/{roster.pk}")
        expected = RosterSerializer(roster)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_get_rosters(self):
        """Get rosters test"""
        url = f"/rosters?user={self.rosteruser.pk}"
        response = self.client.get(url)
        rosters = Roster.objects.filter(user=self.rosteruser)
        expected = RosterSerializer(rosters, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_update_roster(self):
        """Update roster test"""
        roster = Roster.objects.first()
        url = f"/rosters/{roster.pk}"
        data = {
            "name": "Test Roster",
            "user": self.rosteruser.pk
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(None, response.data)
    def test_create_roster_no_name(self):
        """Create roster no name test"""
        url = "/rosters"
        data = {
            "user": self.rosteruser.pk
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data["user"], response.data["user"])
    def test_delete_roster(self):
        """Delete roster test"""
        roster = Roster.objects.first()
        url = f"/rosters/{roster.pk}"
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(None, response.data)
    def test_delete_roster_not_found(self):
        """Delete roster not found test"""
        url = f"/rosters/0"
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
    def test_get_roster_not_found(self):
        """Get roster not found test"""
        url = f"/rosters/0"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
    def test_get_rosters_by_user(self):
        """Get rosters by user test"""
        url = f"/rosters?user={self.rosteruser.pk}"
        response = self.client.get(url)
        rosters = Roster.objects.filter(user=self.rosteruser.pk)
        expected = RosterSerializer(rosters, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_get_rosters_by_user_not_found(self):
        """Get rosters by user not found test"""
        url = f"/rosters?user=0"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)