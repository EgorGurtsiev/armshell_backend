from django.contrib import admin
from django.urls import path, include


api = [
    path('auth/', include('src.custom_auth.urls')),
]

urlpatterns = [
    path('site-admin/', admin.site.urls),
    path('players/', include('src.player.urls')),
    path('company/', include('src.company.urls')),
    path('clan/', include('src.clan.urls')),

    path('api/', include(api)),
]
