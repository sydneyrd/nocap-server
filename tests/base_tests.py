from django.test import TestCase
from rest_framework.authtoken.models import Token
from nocapapi.models import  RosterUser, Character, Weapon, Faction, Role, Server
from tests.character_tests import CharacterTests
from tests.weapon_tests import WeaponTests
from tests.role_tests import RoleTests
from tests.server_tests import ServerTests
from tests.faction_tests import FactionTests
from tests.roster_tests import RosterTests
from tests.calculated_roster_tests import CalculatedRosterTests
from tests.calculated_roster_choice_tests import CalculatedRosterChoicesTests
from tests.char_link_tests import CharLinkTests
from tests.roster_choices_tests import RosterChoicesTests
from tests.roster_user_tests import RosterUserTests
from tests.filter_tests import FilterTests
from tests.public_tests import PublicTests
import collections


class BaseTestCase(TestCase):
    fixtures = ['users', 'tokens', 'rosterusers',  'weapons', 'factions', 'roles', 'servers', 'characters', 'rosters', 'calculated_rosters', 'calculated_roster_choices', 'roster_choices']

# Assuming 'character' is a Character model instance
    character_dict = None
    def setUp(self):
        """Grab the first rosteruser object from the database and add their token to the headers"""
        self.rosteruser = RosterUser.objects.first()
        token = Token.objects.get(user=self.rosteruser.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        character = Character.objects.create(
            role=Role.objects.last(),
            faction=Faction.objects.last(),
            primary_weapon=Weapon.objects.last(),
            secondary_weapon=Weapon.objects.last(),
            server=Server.objects.last(),
            character_name='Test Character',
            user=self.rosteruser,
            notes='Test notes',
            image=None
        )
        # Create an OrderedDict from the test Character instance
        self.character_dict = collections.OrderedDict([
            ('id', character.pk),
            ('role', character.role),
            ('faction', character.faction),
            ('primary_weapon', character.primary_weapon),
            ('secondary_weapon', character.secondary_weapon),
            ('server', character.server),
            ('character_name', character.character_name),
            ('user', character.user),
            ('notes', character.notes),
            ('image', character.image)
        ])

    # I was never even calling this function, but I'm leaving it here in case I do develop a need for a setup that can be used by all the tests, and I don't want to have to rewrite it.

class MyTestCase(BaseTestCase, CharacterTests, WeaponTests, RoleTests, ServerTests, FactionTests, RosterTests, CalculatedRosterTests, CalculatedRosterChoicesTests, CharLinkTests, RosterChoicesTests, RosterUserTests, FilterTests, PublicTests):
    pass
