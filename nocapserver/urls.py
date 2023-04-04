from django.conf import settings
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.conf.urls.static import static
from nocapapi.views import CharacterView, register_user, login_user, CharLinkView, FactionView, ServerView, WeaponView, RoleView, RosterView, UserView, CalculatedRosterView, CalculatedRosterChoicesView, RosterChoicesView, RosterUserView, public_calculated_rosters, public_calculated_roster_choices


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'characters', CharacterView, 'character')
router.register(r'factions', FactionView, 'faction')
router.register(r'servers', ServerView, 'server')
router.register(r'weapons', WeaponView, 'weapon')
router.register(r'roles', RoleView, 'role')
router.register(r'rosters', RosterView, 'roster')
router.register(r'calculatedrosters', CalculatedRosterView, 'calculatedroster')
router.register(r'calculatedrosterchoices',
                CalculatedRosterChoicesView, 'calculatedrosterchoice')
router.register(r'rosterchoices', RosterChoicesView, 'rosterchoice')
router.register(r'rosterusers', RosterUserView, 'rosteruser')
router.register(r'users', UserView, 'user')
router.register(r'links', CharLinkView, 'links')




urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
     path('public-rosters', public_calculated_rosters, name='public-rosters'),
     path('public-roster-choices', public_calculated_roster_choices, name='public-roster-choices'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
