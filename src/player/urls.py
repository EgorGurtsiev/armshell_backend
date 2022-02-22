from django.urls import path

from . import views, apiview

urlpatterns = [
    path('search/', apiview.search_player, name='search_player'),
    path('<str:nickname>/', views.StatsView.as_view(), name='stats'),
]
