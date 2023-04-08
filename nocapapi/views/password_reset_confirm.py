from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
import jwt
from jwt.exceptions import ExpiredSignatureError, DecodeError
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.conf import settings

@csrf_exempt
def password_reset_confirm(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            token = data.get('pass_token')
            new_password = data.get('password')
        except ValueError:
            return JsonResponse({"error": "Invalid data provided"}, status=400)

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get('user_id')
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except (ExpiredSignatureError, DecodeError):
            return JsonResponse({"error": "Invalid or expired token"}, status=400)

        if new_password:
            user.password = make_password(new_password)
            user.save()
            return JsonResponse({"message": "Password has been successfully reset"}, status=200)
        else:
            return JsonResponse({"error": "New password is missing"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
