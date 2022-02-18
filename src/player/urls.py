from django.urls import path

from . import views

urlpatterns = [
    path('<str:nickname>/', views.StatsView.as_view(), name='stats'),
#    path('ajax/search_player/', views.SearchPlayer.as_view(), name='search_player'),
]
