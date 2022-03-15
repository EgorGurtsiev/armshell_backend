from django.urls import path

from . import views, apiview

urlpatterns = [
    path('search/', apiview.search_player, name='search_player'),
    path('<str:nickname>/', views.StatsView.as_view(), name='stats'),
    path('call/busy/', views.SearchForPlayerInClans.as_view(), name='search_for_players_in_clans'),
   # path('call/busy?<str:key_words>'. views.SearchForPlayerInClans.as_view(), name='search_for_players_in_clans')
]
