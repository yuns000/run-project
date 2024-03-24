from django.contrib.auth.hashers import check_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class Account:
    def login(self, email: str, password: str):
        user = User.objects.filter(email=email).first()
        if user is not None and check_password(password, user.password):
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            access_token = jwt_encode_handler(payload)
            refresh_token = str(RefreshToken.for_user(user))
            success = True
            message = f'{email} : login success'
        else:
            success = False
            message = 'Email or password is incorrect'
        return Response({'success': success, 'message': message, "access_token": access_token, "refresh_token": refresh_token})
    
    def account_creation(self, email: str, password: str, username: str, location: str):
        if User.objects.filter(email=email).exists():
            message = 'Email already exists'
            success = False
        else:
            User.create_user(email, password, username, location)
            message = 'success'
            success = True
        return Response({'success': success, 'message': message})