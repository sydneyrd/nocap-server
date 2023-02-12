from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from nocapapi.models import Character, RosterUser, Server, Role, Faction, Weapon
from nocapapi.views.character import CharacterSerializer

class CharacterTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'rosterusers',  'weapons', 'factions', 'roles', 'servers', 'characters',]
    
    def setUp(self):
        # Grab the first Gamer object from the database and add their token to the headers
        self.rosteruser = RosterUser.objects.first()
        token = Token.objects.get(user=self.rosteruser.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_character(self):
        """Create character test"""
        url = "/characters"

        # Define the Game properties
        # The keys should match what the create method is expecting
        # Make sure this matches the code you have
        character = {
            "character_name": "creep test",
            "notes": "hi",
            "image": None,
            "user": self.rosteruser.pk,
            "faction": Faction.objects.first().pk,
            "role": Role.objects.first().pk,
            "primary_weapon": Weapon.objects.first().pk,
            "secondary_weapon": Weapon.objects.first().pk,
            "server": Server.objects.first().pk
        }
        response = self.client.post(url, character, format='json')
        # The _expected_ output should come first when using an assertion with 2 arguments
        # The _actual_ output will be the second argument
        # We _expect_ the status to be status.HTTP_201_CREATED and it _actually_ was response.status_code
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
        # Get the last game added to the database, it should be the one just created
        new_character = Character.objects.last()

        # Since the create method should return the serialized version of the newly created game,
        # Use the serializer you're using in the create method to serialize the "new_game"
        # Depending on your code this might be different
        expected = CharacterSerializer(new_character)

        # Now we can test that the expected ouput matches what was actually returned
        self.assertEqual(expected.data, response.data)