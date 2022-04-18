from django.urls import path

from .endpoints import views, ajax

urlpatterns = [
    path('search/', ajax.search_busy_player, name='search_player'),
    path('<str:nickname>/', views.StatsView.as_view(), name='stats'),
    path('call/busy/', views.SearchPlayerInOtherClans.as_view(), name='search_for_players_in_other_clans'),
]
