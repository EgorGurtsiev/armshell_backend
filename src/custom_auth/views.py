from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from services.wot_api.auth import AuthLogin


@api_view(['GET'])
def get_wgopenid_url(request):
    url = AuthLogin(redirect_uri=request.build_absolute_uri(reverse('login'))).get_response()
    return Response(data={'location': url['data']['location']})
