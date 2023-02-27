from rest_framework import status
from rest_framework.test import APITestCase
from nocapapi.models import Character, Server, Role, Faction, Weapon, RosterUser
from nocapapi.views.character import CharacterSerializer

class CharacterTests(APITestCase):
    def test_create_character(self):
        """Create character test"""
        url = "/characters"
        character = {
            "character_name": "creep test",
            "notes": "hi",
            "user": self.rosteruser.pk,
            "faction": Faction.objects.first().pk,
            "role": Role.objects.first().pk,
            "primary_weapon": Weapon.objects.first().pk,
            "secondary_weapon": Weapon.objects.first().pk,
            "server": Server.objects.first().pk
        }
        response = self.client.post(url, character, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        new_character = Character.objects.last()
        expected = CharacterSerializer(new_character)
        self.assertEqual(expected.data, response.data)

    def test_get_characters(self):
        """Get characters test"""
        url = "/characters"
        response = self.client.get(url)
        characters = Character.objects.all()
        expected = CharacterSerializer(characters, many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_get_character(self):
        """Get single character test"""
        character = Character.objects.first()
        response = self.client.get(f"/characters/{character.pk}")
        expected = CharacterSerializer(character)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected.data, response.data)
    def test_change_character(self):
        """Change character test"""
        character = Character.objects.first()
        url = f"/characters/{character.pk}"
        new_character = {
            "character_name": "creeper test",
            "notes": "hi",
            "user": self.rosteruser.pk,
            "faction": Faction.objects.first().pk,
            "role": Role.objects.first().pk,
            "primary_weapon": Weapon.objects.first().pk,
            "secondary_weapon": Weapon.objects.first().pk,
            "server": Server.objects.first().pk,
            "id": character.pk
        }
        response = self.client.put(url, new_character, format='json')
        character.refresh_from_db()
        self.assertEqual(character.character_name, new_character["character_name"])
        self.assertEqual(character.notes, new_character["notes"])
        self.assertEqual(character.user_id, new_character["user"])
        self.assertEqual(character.faction_id, new_character["faction"])
        self.assertEqual(character.role_id, new_character["role"])
        self.assertEqual(character.primary_weapon_id, new_character["primary_weapon"])
        self.assertEqual(character.secondary_weapon_id, new_character["secondary_weapon"])
        self.assertEqual(character.server_id, new_character["server"])
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
    def test_delete_character(self):
        """Delete character test"""
        character = Character.objects.first()
        url = f"/characters/{character.pk}"
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertFalse(Character.objects.filter(pk=character.pk).exists())
