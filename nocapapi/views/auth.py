from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from nocapapi.models import RosterUser
from rest_framework import status
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework.throttling import AnonRateThrottle
import re


def validate_username(username):
    if len(username) < 4:
        raise ValidationError("Username must be at least 4 characters long.")
    if len(username) > 20:
        raise ValidationError("Username must be no more than 20 characters long.")
    if not username.isalnum():
        raise ValidationError("Username must only contain alphanumeric characters.")
    if re.search(r'\d{3,}', username):
        raise ValidationError("Username must not have more than 2 consecutive digits.")
    if User.objects.filter(username=username).exists():
        raise ValidationError("Username already exists.")




@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def login_user(request):
    '''Handles the authentication of a gamer
    Method arguments:
    request -- The full HTTP request object
    '''
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    authenticated_user = authenticate(username=username, password=password)
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'userId': authenticated_user.id,
            'email': authenticated_user.email
        }
        return Response(data, status=status.HTTP_200_OK)
    else:
        data = {'valid': False}
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AnonRateThrottle])
def register_user(request):
    '''Handles the creation of a new gamer for authentication
    Method arguments:
    request -- The full HTTP request object
    '''
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if not username or not password or not email:
        return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        validate_email(email)
    except ValidationError as e:
        return Response({'error': 'Invalid email address'}, status=status.HTTP_400_BAD_REQUEST)    
    try:
        validate_username(username)
    except ValidationError as e:
        return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
    try:
        validate_password(password)
    except ValidationError as e:
        return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already in use'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        validate_password(request.data['password'])
    except ValidationError as e:
        return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
    email=request.data['email']
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already in use'}, status=status.HTTP_400_BAD_REQUEST)
    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        email=request.data['email']
    )
    rosteruser = RosterUser.objects.create(
        user=new_user
    )
    token = Token.objects.create(user=rosteruser.user)
    data = {'token': token.key}
    return Response(data, status=status.HTTP_201_CREATED)