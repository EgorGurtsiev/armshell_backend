from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('<str:nickname>/', views.StatsView.as_view(), name='stats'),
]