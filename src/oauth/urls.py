from django.urls import path
from .endpoint import views, api_views


urlpatterns = [
    path('register_request/', views.get_url, name='url_to_OpenID'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
