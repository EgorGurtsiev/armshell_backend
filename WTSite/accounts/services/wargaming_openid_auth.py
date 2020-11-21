from openid_wargaming.authentication import Authentication
from openid_wargaming.verification import Verification, OpenIDVerificationFailed

from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login
from django.http.response import HttpResponse

import requests
import datetime
import re

from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()


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


def create_user(nickname, access_token):
    """Создает нового User, или возвращает существующего."""

    try:
        user = User.objects.get(username__exact=nickname)

    except ObjectDoesNotExist:

        password = User.objects.make_random_password(length=25)
        user = User.objects.create_user(nickname, '', password)
        user = get_new_access_token(user, access_token)
        user.save()

    return user


def openid_response_verification(request):
    """Проверяет данные аккаунта с помощью доп. запросов к API"""

    nickname = request.GET['nickname']
    account_id = request.GET['account_id']

    if request.GET['status'] == 'ok':

        data = {
            'application_id': settings.APPLICATION_ID,
            'account_id': request.GET['access_token'],
            'fields': ['nickname', 'private'],
            'extra': ['private.rented']
        }
        response = requests.post(url='https://api.worldoftanks.ru/wot/account/info/', data=data)
        if response.json()['status'] == 'ok':
            if nickname == response.json()['data'][account_id]['nickname']:
                return True
    return Exception


def get_new_access_token(user, access_token=None):
    """"Возвращает новый access_token сроком на 2 недели. В случае ошибки выбрасывает Exception."""

    if not access_token:
        access_token = user.access_token

    data = {
        'application_id': settings.APPLICATION_ID,
        'access_token': access_token
    }
    response = requests.post(url='https://api.worldoftanks.ru/wot/auth/prolongate/', data=data)
    if response.json()['status'] == 'ok':
        user.access_token = response.json()['data']['access_token']
        user.expires_at = datetime.datetime.fromtimestamp(response.json()['data']['expires_at'])
        return user
    return Exception
