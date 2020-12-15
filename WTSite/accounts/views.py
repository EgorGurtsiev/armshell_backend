from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .services.wargaming_openid_auth import get_url_to_auth, create_user, openid_response_verification,\
    get_new_access_token


def login_user_step1(request):
    url = get_url_to_auth(request)
    url_back = request.GET['url_back']
    response = redirect(url)
    response.set_cookie(key='url_back', value=url_back, path=reverse('callback'),
                        httponly=True)
    return response


def login_user_step2(request):
    if openid_response_verification(request):

        user = create_user(request.GET['nickname'], request.GET['account_id'], request.GET['access_token'])
        login(request, user)
        # user.access_token = new_access_token  --------------------------------------------------
        # user.save()

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
