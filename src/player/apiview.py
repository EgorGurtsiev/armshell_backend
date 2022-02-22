from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.wot_api.account import AccountList


@api_view(['GET'])
def search_player(request):
    data = AccountList(search=request.query_params['nickname'], limit=3).get_response()['data']
    return Response(data)

