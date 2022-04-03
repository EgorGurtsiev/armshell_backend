from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from services.wot_api.stronghold import ActivateClanReserve


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def activate_reserve(request):
    if request.user.is_officer:
        ActivateClanReserve(request.user.access_token, request.query_params['level'],
                            request.query_params['type']).get_response()['data']['activated_at']

