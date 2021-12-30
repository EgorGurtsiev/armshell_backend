from django.shortcuts import render
from .services.reserves import get_dict_reserves, formatting_for_issue
from django.contrib.auth import get_user_model
User = get_user_model()


def reserves(request):
    template_name = 'clan/reserves.html'
    context = {}
    user = User.objects.get(username=str(request.user))
    data = get_dict_reserves(user.access_token)
    data = formatting_for_issue(data)
    context['data'] = data
    return render(request, template_name, context)
