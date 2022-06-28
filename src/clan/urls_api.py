from django.urls import path, include

from . import views_api

urlpatterns = [
    path('my_clan/reserves/', views_api.activate_reserve, name='reserves_list'),
    path('my_clan/reserves/activate/', views_api.reserves_list, name='activate_reserve')
]
