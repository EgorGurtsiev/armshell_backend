from .services.reserves import get_dict_reserves, formatting_for_issue
from django.views.generic.base import TemplateView

from ..player.models import Player as User


class Reserves(TemplateView):

    template_name = "clan/reserves.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = User.objects.get(username=str(self.request.user))
        data = get_dict_reserves(player.access_token)
        data = formatting_for_issue(data)
        context['data'] = data
        print(data)
        return context
