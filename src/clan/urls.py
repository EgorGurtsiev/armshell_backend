from django.urls import path

from . import views

urlpatterns = [
    path('reserves/', views.Reserves.as_view(), name='reserves'),
]