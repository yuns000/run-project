from django.contrib.auth.hashers import check_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from .Account import Account
from .models import User
from .serializers import (AccountCreationSerializer, LoginSerializer,
                          UserSerializer)

ACCOUNTS_TAG = 'accounts'
class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    obj_account = Account()

    @swagger_auto_schema(request_body=LoginSerializer, tags=[ACCOUNTS_TAG])
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        return self.obj_account.login(email, password)

    @swagger_auto_schema(request_body=AccountCreationSerializer, tags=[ACCOUNTS_TAG])
    @action(detail=False, methods=['post'])
    def account_creation(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        location = request.data.get('location')
        
        return self.obj_account.account_creation(email, password, username, location)