from rest_framework import status
from rest_framework.test import APITestCase
import json
from collections import OrderedDict

class FilterTests(APITestCase):
    def test_filter_characters_name_only(self):
        url = '/characters?search_text=ihaveanamenow'
    
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'ihaveanamenow')
        self.assertIsInstance(response.data, list)

    def test_filter_by_role(self):
        url = '/characters?role=1'

        response = self.client.get(url)
        print(response)
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_characters_name_with_space(self):
        url = '/characters?search_text=the%20Storr'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'The Storrm')