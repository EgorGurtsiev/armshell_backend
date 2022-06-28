from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from services.wot_api.auth import AuthLogin
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout


def get_url(request):
    try:
        next_ = request.GET['next']
    except:
        next_ = reverse('home')

    components = {
        'scheme': request.scheme,
        'host': request.get_host(),
        'path': reverse('login'),
        'next': next_
    }
    redirect_uri = '{scheme}://{host}{path}?next={next}'.format(**components)
    url = AuthLogin(redirect_uri=redirect_uri).get_response()
    url = url['data']['location']
    return redirect(url)


@api_view()
def get_auth_url(request):
    try:
        next_ = request.GET['next']
    except:
        next_ = reverse('home')

    components = {
        'scheme': request.scheme,
        'host': request.get_host(),
        'path': reverse('login'),
        'next': next_
    }
    redirect_uri = '{scheme}://{host}{path}?next={next}'.format(**components)
    url = AuthLogin(redirect_uri=redirect_uri).get_response()
    url = url['data']['location']
    return Response(data=url)


def login(request):
    user = authenticate(request)
    if user is None:
        return HttpResponse('Авторизация не прошла!')

    auth_login(request, user)
    return redirect(request.GET['next'])


def logout(request):
    auth_logout(request)

    url_back = request.GET['next']
    return redirect(url_back)

