
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework import routers
from nocapapi.views import CharacterView, register_user, login_user, CharLinkView, FactionView, ServerView, WeaponView, RoleView, RosterView, UserView, CalculatedRosterView, CalculatedRosterChoicesView, RosterChoicesView, RosterUserView


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
router.register(r'links', CharLinkView, 'link')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="reset_password.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="reset_password_sent.html"), name='reset_password_sent'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_done.html"), name='password_reset_done')
]
