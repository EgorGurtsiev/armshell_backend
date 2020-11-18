import re

from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden

from openid_wargaming.verification import Verification
from openid_wargaming.exceptions import OpenIDVerificationFailed

from .services.wargaming_openid_auth import get_url_to_auth, create_user, openid_response_verification,\
    get_new_access_token

from django.conf import settings


def login_user_step1(request):
    url = get_url_to_auth(request)
    url_before_authorization = request.GET['url_back']
    response = redirect(url)
    response.set_cookie(key='url_before_authorization', value=url_before_authorization, path=reverse('callback'),
                        httponly=True)
    return response


def login_user_step2(request):
    if openid_response_verification(request):
        new_access_token = get_new_access_token(request.GET['access_token'])
        # User.access_token = new_access_token
        print(new_access_token)

        user = create_user(request.GET['nickname'])
        login(request, user)

        url_back = request.COOKIES['url_back']
        response = redirect(url_back)
        response.delete_cookie('url_back')
        return response
    else:
        logout(request)
        return HttpResponse('Forbidden')


def logout_user(request):
    logout(request)

    url_back = request.GET['url_back']
    response = redirect(url_back)
    return response
