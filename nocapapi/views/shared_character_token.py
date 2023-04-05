from rest_framework.decorators import api_view
from rest_framework.response import Response
from nocapapi.models import SharedCharacterToken
from nocapapi.models import RosterUser

@api_view(['GET'])
def generate_shared_character_token(request):
    rosteruser = RosterUser.objects.get(user_id=request.auth.user)
    if SharedCharacterToken.objects.filter(user=rosteruser).exists():
        shared_character_token = SharedCharacterToken.objects.get(user=rosteruser)
        shared_character_token.delete()
    shared_character_token = SharedCharacterToken.objects.create(user=rosteruser)
    return Response({'token': str(shared_character_token.token)})
