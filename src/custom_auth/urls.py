from django.urls import path, include
from src.custom_auth.views import get_wgopenid_url


urlpatterns = [
    path('get_openid_location/', get_wgopenid_url, name='url_to_OpenID'),
    path('session/', include('src.custom_auth.session.urls')),
    #  path('jwt/', include('src.auth.jwt.urls'))
]
