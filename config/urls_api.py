from django.urls import path, include


urlpatterns = [
    path('v1/clans/', include('src.clan.urls_api')),
    # path('v1/players/', include('src.player.urls_api')),
]
