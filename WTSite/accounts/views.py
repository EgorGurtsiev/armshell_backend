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
import requests


def login_user_step1(request):
    url = get_url_to_auth(request)
    url_before_authorization = request.GET.get('url_before_authorization', reverse('home'))
    response = redirect(url)
    response.set_cookie(key='url_before_authorization', value=url_before_authorization, path=reverse('callback'))
    return response


def login_user_step2(request):
    if openid_response_verification(request):
        get_new_access_token(request.GET['data']['access_token'])
        # -------------------------------------------------------------------------
        url_back = request.COOKIES['url_before_authorization']
        request.delete_cookie(key='url_before_authorization', path=reverse('callback'))
        create_user(request.GET['nickname'], request)
    else:
        logout(request)
        return HttpResponse('Forbidden')
    return redirect(url_back)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
