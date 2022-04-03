from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import SearchForm
from .services.search import SearchPlayerInClans
from .services.stats import tanks_stats, account_search
from services.wot_api.wot_api import ExceptionAPI
from services.wot_api.tanks import TanksStats
from .models import Player as User


class StatsView(TemplateView):
    """Это view должно отображать общюю абс-статистику игрока"""

    template_name = 'stats/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            stats = tanks_stats(account_id=account_search(nickname=self.kwargs['nickname']),
                                tank_id="57937, 15617, 19009, 19969, 22017, 15697, 4737, 3681")
        except ExceptionAPI as err:
            context['status'] = "error"
            context['massage'] = err.args
            return context
        context['status'] = "ok"
        context['data'] = stats['data']
        return context


# class MyStats(TemplateView):
#     """
#     Подробная статистика игрока.
#     Нереализованно: в случае если пользователь не авторизован необходимо вернуть страницу с обобзеной статистикой игрока
#     + сообщение о необходимости авторизации для просмотра подробной статистики.
#     """
#     template_name = 'stats/my_stats.html'
#
#     def get(self, request):
#         context = self.get_context_data()
#         try:
#             user = User.objects.get(username=str(request.user))
#         except:
#             context['status'] = 'error'
#             context['massage'] = 'Ошибка авторизации пользователя!'
#             return self.render_to_response(context)
#         stats = TanksStats(account_id=user.account_id,
#                            tank_id="57937, 15617, 19009, 19969, 22017, 15697, 4737, 3681").get_response()
#         if stats['status'] == "ок":
#             context['data'] = {}
#             context['data']['nickname'] = user.username
#             context['data']['stats'] = {}
#             actual_stats = stats['data']
#             context['data']['stats'] = actual_stats['stats']
#             # for tank in stats['data']['stats']:
#             #     context['data']['stats'] += tank
#
#             context['status'] = 'ok'
#         else:
#             context['status'] = 'warning'
#             context['massage'] = 'Ошибка загрузки данных с сервера wargaming'
#         return self.render_to_response(context)


class SearchForPlayerInOtherClans(TemplateView):
    template_name = 'player/search_busy_player.html'
    is_list = False

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            result = cache.get(form.search)
            if not result:
                result = SearchPlayerInClans(search=request.POST.get('search')).get_players_list()
                cache.set(form.search, result, 1)
            return HttpResponseRedirect('?page=1')
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('page'):
            data = ['askdsf', 'asdfasdf', 'asdf', 'askdsf', 'asdfasdf', 'askdsf', 'asdfasdf', 'askdsf', 'asdfasdf', 'askdsf', 'asdfasdf']
            paginator = Paginator(data, 4)

            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['page_obj'] = page_obj
        return context



#
# def search_players_in_other_clan(request, search):
#     test_player_list = [{
#         'account_id': 6511,
#         "last_battle_time": 1648161857,
#         "battles_in_clan_wars": 213,
#         "stats": [{
#             "tank_id": 12332,
#             "random": {
#                 "avg_damage": 755,
#                 "battles": 755,
#                 "percent_win": 587,
#                 },
#             "stronghold_skirmish": {
#                 "avg_damage": 755,
#                 "battles": 755,
#                 "percent_win": 587,
#                 },
#             "stronghold_defense": {
#                 "avg_damage": 755,
#                 "battles": 755,
#                 "percent_win": 587,
#                 },
#             "globalmap_absolute": {
#                 "avg_damage": 755,
#                 "battles": 755,
#                 "percent_win": 587,
#                 },
#             }, {
#                 "tank_id": 2131,
#                 "random": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "stronghold_skirmish": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "stronghold_defense": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "globalmap_absolute": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#             }, {
#                 "tank_id": 2332,
#                 "random": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "stronghold_skirmish": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "stronghold_defense": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "globalmap_absolute": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#             }]
#         }, {
#         'account_id': 6848,
#         "last_battle_time": 1648161857,
#         "battles_in_clan_wars": 213,
#         "stats": [{
#             "tank_id": 12332,
#             "random": {
#                 "avg_damage": 755,
#                 "battles": 755,
#                 "percent_win": 587,
#                 },
#             "stronghold_skirmish": {
#                 "avg_damage": 755,
#                 "battles": 755,
#                 "percent_win": 587,
#                 },
#             "stronghold_defense": {
#                 "avg_damage": 755,
#                 "battles": 755,
#                 "percent_win": 587,
#                 },
#             "globalmap_absolute": {
#                 "avg_damage": 755,
#                 "battles": 755,
#                 "percent_win": 587,
#                 },
#             }, {
#                 "tank_id": 2131,
#                 "random": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "stronghold_skirmish": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "stronghold_defense": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "globalmap_absolute": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#             }, {
#                 "tank_id": 2332,
#                 "random": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "stronghold_skirmish": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "stronghold_defense": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#                 "globalmap_absolute": {
#                     "avg_damage": 755,
#                     "battles": 755,
#                     "percent_win": 587,
#                 },
#             }]
#         },
#     ]
#     return JsonResponse(SearchPlayerInClans(test_player_list).get_players_list())
#     # return JsonResponse(SearchPlayerInClans(search).get_players_list())
