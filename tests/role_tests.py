from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import  Role
from nocapapi.views.role import RoleSerializer

class RoleTests(APITestCase):
    def test_get_roles(self):
        """Get roles test"""
        url = "/roles"
        response = self.client.get(url)
        roles = Role.objects.all()
        expected = RoleSerializer(roles, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)