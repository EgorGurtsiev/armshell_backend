from django.urls import path
from .views import RegdCompany#, DelCompany


urlpatterns = [
    path('add/', RegdCompany.as_view(), name='new-company'),
    #path('delete/', DelCompany.as_view(), 'del-company'),
]