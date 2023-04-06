from rest_framework.decorators import api_view
from rest_framework.response import Response
from nocapapi.models import SharedCalculatedRosterChoiceToken
from nocapapi.models import RosterUser, CalculatedRoster
from rest_framework import status

@api_view(['GET'])
def generate_shared_calculated_roster_token(request):
    try:  
        rosteruser = RosterUser.objects.get(user_id=request.auth.user)
        calculated_roster = CalculatedRoster.objects.get(pk=request.data['roster'])
        if calculated_roster.user != rosteruser:
            return Response({'message': 'You do not have permission to share this roster'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            
                if SharedCalculatedRosterChoiceToken.objects.filter(calculated_roster=calculated_roster).exists():
                    shared_calculated_roster_choice_token = SharedCalculatedRosterChoiceToken.objects.get(user=rosteruser)
                    shared_calculated_roster_choice_token.delete()
                shared_calculated_roster_choice_token = SharedCalculatedRosterChoiceToken.objects.create(user=rosteruser, calculated_roster=calculated_roster)
                return Response({'token': str(shared_calculated_roster_choice_token.token)})
    except Exception as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
