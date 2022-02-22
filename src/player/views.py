from django.shortcuts import render
from django.views.generic.base import TemplateView

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


class MyStats(TemplateView):
    """
    Подробная статистика игрока.
    Нереализованно: в случае если пользователь не авторизован необходимо вернуть страницу с обобзеной статистикой игрока
    + сообщение о необходимости авторизации для просмотра подробной статистики.
    """
    template_name = 'stats/my_stats.html'

    def get(self, request):
        context = self.get_context_data()
        try:
            user = User.objects.get(username=str(request.user))
        except:
            context['status'] = 'error'
            context['massage'] = 'Ошибка авторизации пользователя!'
            return self.render_to_response(context)
        stats = TanksStats(account_id=user.account_id,
                           tank_id="57937, 15617, 19009, 19969, 22017, 15697, 4737, 3681").get_response()
        if stats['status'] == "ок":
            context['data'] = {}
            context['data']['nickname'] = user.username
            context['data']['stats'] = {}
            actual_stats = stats['data']
            context['data']['stats'] = actual_stats['stats']
            # for tank in stats['data']['stats']:
            #     context['data']['stats'] += tank

            context['status'] = 'ok'
        else:
            context['status'] = 'warning'
            context['massage'] = 'Ошибка загрузки данных с сервера wargaming'
        return self.render_to_response(context)


