from django.urls import path

from . import views

urlpatterns = [
    path('reserves/', views.reserves, name='reserves'),
]