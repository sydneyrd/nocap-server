
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from nocapapi.views import CharacterView, register_user, login_user, FactionView, ServerView, WeaponView, RoleView, RosterView, UserView, CalculatedRosterView, CalculatedRosterChoicesView, RosterChoicesView, RosterUserView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'characters', CharacterView, 'character')
router.register(r'factions', FactionView, 'faction')
router.register(r'servers', ServerView, 'server')
router.register(r'weapons', WeaponView, 'weapon')
router.register(r'roles', RoleView, 'role')
router.register(r'rosters', RosterView, 'roster')
router.register(r'calculatedrosters', CalculatedRosterView, 'calculatedroster')
router.register(r'calculatedrosterchoices', CalculatedRosterChoicesView, 'calculatedrosterchoice')
router.register(r'rosterchoices', RosterChoicesView, 'rosterchoice')
router.register(r'rosterusers', RosterUserView, 'rosteruser')
router.register(r'users', UserView, 'user')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]