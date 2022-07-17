import re

from rest_framework import serializers
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer


class WGOpenIdDataSerializer(serializers.Serializer):
    access_token = serializers.CharField(min_length=40, max_length=40)
    nickname = serializers.CharField(min_length=3, max_length=24)
    account_id = serializers.CharField(min_length=2, max_length=8)
    expires_at = serializers.DateTimeField()


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken('No valid token found in cookie \'refresh_token\'')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token