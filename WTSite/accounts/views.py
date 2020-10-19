from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect

from django.conf import settings


def openid_wg_login(request):
    if request.method == 'GET':
        application_id = settings.APPLICATION_ID
        wg_api_request = HttpRequest
        wg_api_request.method = 'POST'
        wg_api_request.path = '/wot/auth/login/'
        wg_api_request.
        #("https://api.worldoftanks.ru/wot/auth/login/?"
        #                              "application_id=" + application_id +
        #                              "&expires_at=1209600&redirect_uri=http://127.0.0.1:8000/", data=request.POST)
        return HttpResponseRedirect(wg_api_request)
    if request.method == 'POST':
        pass


def logout():
    pass
