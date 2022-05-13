from django.urls import path

from .endpoints import views, ajax_view


# Ajax view
urlpatterns = [
    path('search/', ajax_view.search_player),
    path('call/busy/search/', ajax_view.search_busy_player, name='search_busy_player'),
]
# Django view
urlpatterns += [
    path('call/busy/', views.SearchPlayerInOtherClans.as_view(), name='search_for_players_in_other_clans'),
    path('<str:nickname>/', views.StatsView.as_view(), name='stats')
]
