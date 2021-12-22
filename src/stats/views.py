from django.shortcuts import render
from django.views.generic.base import TemplateView

from .services.stats import tanks_stats, account_search

from django.contrib.auth import get_user_model
User = get_user_model()


class StatsView(TemplateView):
    """Это view должно отображать общюю абс-статистику игрока"""

    template_name = 'stats/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        account_id = account_search(nickname=self.kwargs['nickname'])

        if isinstance(account_id, str):
            context['error'] = account_id
        else:
            stats = tanks_stats(account_id=account_id, tank_id="57937, 15617, 19009, 19969, 22017, 15697, 4737, 3681")

            if stats['status'] == "ок":
                context['stats'] = stats['data']
            else:
                context['error'] = stats['error']
        return context


class MyStats(TemplateView):
    pass
