from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.openid_wg_login, name='WG-OpenID'),
    path('logout/', views.logout),
]