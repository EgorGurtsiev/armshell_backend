from openid_wargaming.authentication import Authentication
from openid_wargaming.verification import Verification, OpenIDVerificationFailed

from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http.response import HttpResponse

import requests
import re

from django.conf import settings


def get_url_to_auth(request, return_to=None):
    if not return_to:
        components = {
            'scheme': request.scheme,
            'host': request.get_host(),
            'path': reverse('callback')
        }
        return_to = '{scheme}://{host}{path}'.format(**components)

    api_url = "https://api.worldoftanks.ru/wot/auth/login/"
    application_id = settings.APPLICATION_ID
    data = {
        'application_id': application_id,
        'nofollow': 1,
        'expires_at': 60,
        'redirect_uri': return_to
    }

    res = requests.post(url=api_url, data=data)
    res_json = res.json()
    url = res_json['data']['location']
    return url


def create_user(nickname, request):
    try:
        user = User.objects.get(username__exact=nickname)

    except ObjectDoesNotExist:
        password = User.objects.make_random_password(length=25)
        user = User.objects.create_user(nickname, '', password)
        user.save()

    login(request, user)
    return user


def __parse_openid_response(request):
    """"Парсит данные ответа от openID"""

    if request.GET['status'] == 'ok':
        d_result = {
            'nickname': request.GET['nickname'],
            'account_id': request.GET['account_id'],
            'access_token': request.GET['access_token']
        }
        return d_result
    else:
        return Exception


def openid_response_verification(request):
    """Проверяет данные аккаунта с помощью доп. запросов к API"""

    if request.GET['status'] == 'ok':
        data = __parse_openid_response(request)
        application_id = settings.APPLICATION_ID

        data = {
            'application_id': application_id,
            'account_id': request.GET['data']['access_token'],
            'fields': ['nickname', 'private'],
            'extra': ['private.rented']
        }
        response = requests.post(url='https://api.worldoftanks.ru/wot/account/info/', data=data)
        res_json = response.json()
        if res_json['status'] == 'ok':
            if nickname == response.json()['data'][account_id]['nickname']:
                return True
        return False


        return check_access_token()
    return False


def get_new_access_token(access_token):
    """"Возвращает новый access_token сроком на 2 недели. В случае ошибки выбрасывает Exception."""

    data = {
        'application_id': settings.APPLICATION_ID,
        'access_token': access_token
    }
    response = requests.post(url='https://api.worldoftanks.ru/wot/auth/prolongate/', data=data)
    if response.json()['status'] == 'ok':
        return response.json()['data']['account_id']
    return Exception
