from django.contrib.auth import authenticate
from django.contrib.auth import login, logout as dj_logout
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from src.custom_auth.serializers import LoginSerializer


class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = authenticate(request)
        if user is None:
            return Response('Авторизация не прошла!')

        login(request, user)
        return Response({'status': 'ок'})


@api_view(['POST'])
def logout(request):
    dj_logout(request)
    return Response()
