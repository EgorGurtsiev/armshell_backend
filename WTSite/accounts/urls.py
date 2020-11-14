from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('login/', views.login_user_step1, name='login'),
    path('login/finish/', views.login_user_step2, name='callback'),
    path('logout/', views.logout_user, name='logout'),
    # path('login/error/', views.error, {'code', 'massage'}, name='error'),
]
