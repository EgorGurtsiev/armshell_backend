from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('<str:nickname>/', views.StatsView.as_view(), name='stats'),
    path('my_stats/', views.MyStats.as_view(), name='my_stats')
]