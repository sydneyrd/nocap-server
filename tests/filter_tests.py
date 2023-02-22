from rest_framework import status
from rest_framework.test import APITestCase

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
        self.assertEqual(len(response.data) > 1, True)
        for character in response.data:
            expected_keys = ['id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server', 'character_name', 'user', 'notes', 'image']
            keys = list(self.character_dict.keys())
            self.assertCountEqual(keys, expected_keys)
            self.assertEqual(character['role'], 1)

    def test_filter_characters_name_with_space(self):
        url = '/characters?search_text=the%20Storr'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'The Storrm')
        for character in response.data:
            expected_keys = ['id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server', 'character_name', 'user', 'notes', 'image']
            keys = list(self.character_dict.keys())
            self.assertCountEqual(keys, expected_keys)
    def test_filter_by_server(self):
        url = '/characters?server=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data) > 1, True)
        for character in response.data:
            expected_keys = ['id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server', 'character_name', 'user', 'notes', 'image']
            keys = list(self.character_dict.keys())
            self.assertCountEqual(keys, expected_keys)
            self.assertEqual(character['server'], 1)
    def test_filter_by_faction(self):
        url = '/characters?faction=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data) > 1, True)
        for character in response.data:
            expected_keys = ['id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server', 'character_name', 'user', 'notes', 'image']
            keys = list(self.character_dict.keys())
            self.assertCountEqual(keys, expected_keys)
            self.assertEqual(character['faction'], 1)

    def test_filter_by_primary_weapon(self):
        url = '/characters?primary_weapon=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data) > 1, True)
        for character in response.data:
            expected_keys = ['id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server', 'character_name', 'user', 'notes', 'image']
            keys = list(self.character_dict.keys())
            self.assertCountEqual(keys, expected_keys)
            self.assertEqual(character['primary_weapon'], 1)
    def test_filter_by_secondary_weapon(self):
        url = '/characters?secondary_weapon=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data) > 1, True)
        for character in response.data:
            expected_keys = ['id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server', 'character_name', 'user', 'notes', 'image']
            keys = list(self.character_dict.keys())
            self.assertCountEqual(keys, expected_keys)
            self.assertEqual(character['secondary_weapon'], 1)
    def test_filter_by_primary_weapon_and_secondary_weapon(self):
        url = '/characters?primary_weapon=1&secondary_weapon=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data[0]['character_name'], 'ihaveanamenow')
        for character in response.data:
            expected_keys = ['id', 'role', 'faction', 'primary_weapon', 'secondary_weapon', 'server', 'character_name', 'user', 'notes', 'image']
            keys = list(self.character_dict.keys())
            self.assertCountEqual(keys, expected_keys)
            self.assertEqual(character['primary_weapon'], 1)
            self.assertEqual(character['secondary_weapon'], 1)
    def test_filter_by_primary_weapon_and_secondary_weapon_and_role(self):
        url = '/characters?primary_weapon=1&secondary_weapon=1&role=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'ihaveanamenow')
    def test_filter_by_primary_weapon_and_secondary_weapon_and_role_and_faction(self):
        url = '/characters?primary_weapon=1&secondary_weapon=1&role=1&faction=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'ihaveanamenow')
    def test_filter_by_primary_weapon_and_secondary_weapon_and_role_and_faction_and_server(self):
        url = '/characters?primary_weapon=1&secondary_weapon=1&role=1&faction=1&server=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'ihaveanamenow')
    def test_filter_by_primary_weapon_and_secondary_weapon_and_role_and_faction_and_server_and_name(self):
        url = '/characters?primary_weapon=1&secondary_weapon=1&role=1&faction=1&server=1&search_text=ihaveanamenow'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'ihaveanamenow')
    def test_filter_by_primary_weapon_and_secondary_weapon_and_role_and_faction_and_server_and_name_and_user_id(self):
        url = '/characters?primary_weapon=1&secondary_weapon=1&role=1&faction=1&server=1&search_text=ihaveanamenow&user_id=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'ihaveanamenow')
    def test_filter_by_primary_weapon_and_secondary_weapon_and_role_and_faction_and_server_and_name_and_user_id_and_character_id(self):
        url = '/characters?primary_weapon=1&secondary_weapon=1&role=1&faction=1&server=1&search_text=ihaveanamenow&user_id=1&character_id=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['character_name'], 'ihaveanamenow')
    def test_filter_by_all(self):
        url = '/characters?primary_weapon=1&secondary_weapon=1&role=1&faction=1&server=1&search_text=ihaveanamenow&user_id=1&character_id=1'
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        