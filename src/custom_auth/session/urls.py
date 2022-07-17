from django.urls import path
from src.custom_auth.session.views import Login, logout


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]