from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import SearchPlayersInOtherClansSerializer
from django.core.cache import cache

from services.wot_api.account import AccountList


@api_view(['GET'])
def search_player(request):
    data = AccountList(search=request.query_params['nickname'], limit=3).get_response()['data']
    return Response(data)


@api_view(['POST'])
def search_busy_player(request):
    serializer = SearchPlayersInOtherClansSerializer(data=request.data)

    return Response(data)
    # if serializer.is_valid():
    #     serializer.save()
    #     result = cache.get(serializer.search)
    #     if not result:
    #         result = SearchPlayerInClans(search=request.POST.get('search')).get_players_list()
    #         cache.set(form.search, result, 1)
    #     return HttpResponseRedirect('?page=1')
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.)

    # def post(self, request):
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         result = cache.get(form.search)
    #         if not result:
    #             result = SearchPlayerInClans(search=request.POST.get('search')).get_players_list()
    #             cache.set(form.search, result, 1)
    #         return HttpResponseRedirect('?page=1')
    #     return render(request, self.template_name, {'form': form})