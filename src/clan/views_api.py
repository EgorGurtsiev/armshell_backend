from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from services.wot_api.stronghold import ActivateClanReserve
from ..player.models import Player as User
from src.clan.services.reserves import get_dict_reserves, formatting_for_issue


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reserves_list(request):
    player = User.objects.get(username=str(request.user))
    data = get_dict_reserves(player.access_token)
    data = formatting_for_issue(data)
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def activate_reserve(request):
    if request.user.is_officer:
        data = ActivateClanReserve(request.user.access_token, request.query_params['level'],
                                   request.query_params['type']).get_response()['data']['activated_at']
        return Response(data)
    return Response(data={})
