import re

from rest_framework import serializers


class RedirectUriSerializer(serializers.Serializer):
    redirect_uri = serializers.CharField()

    def validate_redirect_uri(self, uri):
        if re.match(r'https?://armshell\.ru/', uri):
            raise serializers.ValidationError('Передан невалидный URI.')
        return uri


class LoginSerializer(serializers.Serializer):
    access_token = serializers.CharField(min_length=40, max_length=40)
    nickname = serializers.CharField(min_length=3, max_length=24)
    account_id = serializers.CharField(min_length=2, max_length=8)
    expires_at = serializers.DateTimeField()
