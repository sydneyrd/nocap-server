from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
import datetime
import json
import os
from django.conf import settings



@csrf_exempt
def password_reset_request(request):
    if request.method == 'POST':
        
        try:
            email = json.loads(request.body).get('email')
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Handle the case when the email does not exist in the system
            return JsonResponse({"error": "Email address not found"}, status=404)

        user_id = user.id
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

        token = jwt.encode({"user_id": user_id, "exp": expiration_time}, settings.JWT_SECRET_KEY, algorithm="HS256")

        reset_link = f'http://localhost:3000/reset-password/{token}'

        # Send the reset link with the token to the user's email
        send_mail(
            'Password Reset Request',
            f'Click the link below to reset your password:\n\n{reset_link}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return JsonResponse({"message": "Password reset link sent to your email"}, status=200)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
