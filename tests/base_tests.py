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


class BaseTestCase(TestCase):
    fixtures = ['users', 'tokens', 'rosterusers',  'weapons', 'factions', 'roles', 'servers', 'characters', 'rosters', 'calculated_rosters', 'calculated_roster_choices']
    
    def setUp(self):
        """Grab the first rosteruser object from the database and add their token to the headers"""
        self.rosteruser = RosterUser.objects.first()
        token = Token.objects.get(user=self.rosteruser.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")


class MyTestCase(BaseTestCase, CharacterTests, WeaponTests, RoleTests, ServerTests, FactionTests, RosterTests, CalculatedRosterTests, CalculatedRosterChoicesTests):
    pass


