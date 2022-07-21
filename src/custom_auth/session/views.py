from django.contrib.auth import authenticate
from django.contrib.auth import login, logout as dj_logout
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from src.custom_auth.serializers import LoginSerializer


class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = authenticate(
            nickname=request.data['nickname'],
            account_id=request.data['account_id'],
            access_token=request.data['access_token'],
            expires_at=request.data['expires_at']
        )
        if user is None:
            return Response('Авторизация не прошла!', status=HTTP_401_UNAUTHORIZED)

        login(request, user)
        res = Response(status=HTTP_200_OK)
        return res


@api_view(['POST'])
def logout(request):
    dj_logout(request)
    return Response()
