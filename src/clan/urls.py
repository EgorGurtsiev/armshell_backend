from django.urls import path, include

from . import views

urlpatterns = [
    path('reserves/', views.Reserves.as_view(), name='reserves'),

    path('api/', include('src.clan.urls_api'))
]