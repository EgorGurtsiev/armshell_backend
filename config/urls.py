from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('site-admin/', admin.site.urls),
    path('oauth/', include('src.oauth.urls')),

    path('players/', include('src.player.urls')),
    path('company/', include('src.company.urls')),
    path('clan/', include('src.clan.urls')),
    path('', include('src.home.urls')),
]
