from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'location', 'password')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=120)

class AccountCreationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=120)
    username = serializers.CharField(max_length=10)
    location = serializers.CharField(max_length=30)