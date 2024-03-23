from django.contrib.auth.hashers import check_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import (AccountCreationSerializer, LoginSerializer,
                          UserSerializer)


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=LoginSerializer)
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = User.objects.filter(email=email).first()
        if user is not None and check_password(password, user.password):
            request.session['user'] = user.id
            success = True
            message = f'{email} : login success'
        else:
            success = False
            message = 'Email or password is incorrect'
        
        return Response({'success': success, 'message': message})

    @swagger_auto_schema(request_body=AccountCreationSerializer)
    @action(detail=False, methods=['post'])
    def account_creation(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        location = request.data.get('location')
        
        if User.objects.filter(email=email).exists():
            message = 'Email already exists'
            success = False
        else:
            User.create_user(email, password, username, location)
            message = 'success'
            success = True

        return Response({'success': success, 'message' : message})